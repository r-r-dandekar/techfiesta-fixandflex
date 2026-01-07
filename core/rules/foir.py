from core.base_rules import HardRule
from core.user import User
from utils.logs import log_error, log_info
from pydantic import Field

# Ensure HardRule inherits from pydantic.BaseModel
class FOIR(HardRule):
    # Fields defined as type hints (Pydantic handles these)
    max_foir: float
    emi: float
    
    # Optional: Hardcode the rule_type so you don't have to pass it every time
    rule_type: str = "foir"

    def satisfied(self, user: User) -> bool:
        # --- Calculation Logic (remains largely the same) ---
        monthly_fixed_obligations = 0

        existing_obligations = user.info.get("existing_obligations")
        if not existing_obligations:
            log_error("No data available about existing obligations!")
            return False

        # Loans
        loans = existing_obligations.get("loans", [])
        for loan in loans:
            # Note: Fixed a small logic error from your snippet 
            # (using += instead of = to sum all loans)
            monthly_fixed_obligations += loan.get("monthly_emi", 0)
            
        # Credit Card monthly minimums
        credit_cards = existing_obligations.get("credit_cards", [])
        for credit_card in credit_cards:
            monthly_fixed_obligations += credit_card.get("monthly_min_payment", 0)

        # Other monthly expenses
        other = existing_obligations.get("other", [])
        for entry in other:
            if entry.get("is_monthly", False):
                monthly_fixed_obligations += entry.get("amount", 0)

        # self.emi is now a Pydantic-managed attribute
        monthly_fixed_obligations += self.emi

        log_info(f"Monthly Fixed Obligations: {monthly_fixed_obligations}")

        # --- Income Calculation ---
        gross_monthly_income = 0

        employment = user.info.get("employment")
        if employment and employment.get("applicable"):
            gross_monthly_income += employment.get("monthly_gross_salary", 0)
            
        business_info = user.info.get("business_info") # Corrected from 'employment'
        if business_info and business_info.get("applicable"):
            profit = business_info.get("monthly_profit", 0) or 0
            shares = business_info.get("shares_owned_fraction", 0) or 0
            gross_monthly_income += profit * shares

        if gross_monthly_income == 0:
            log_error("No monthly income sources found!")
            return False

        log_info(f"Gross Monthly Income: {gross_monthly_income}")

        foir = monthly_fixed_obligations / gross_monthly_income
        log_info(f"FOIR: {foir}")

        return foir <= self.max_foir