from core.base_rules import HardRule
from core.user import User
from utils.logs import log_error, log_info

# Fixed Obligation to Income Ratio
# a. k. a. Debt Burden
class FOIR(HardRule):

    # Expressed as a percentage e.g. 0.5
    max_foir : float
    
    # EMI of the loan that is to be checked for eligibility
    emi : float

    def satisfied(self, user: User) -> bool:
        # Calculate FOIR based on user info

        # First, find out mothly fixed obligations based on loans,
        # credit card monthly minimums, and rent
        monthly_fixed_obligations = 0

        existing_obligations = user.info.get("existing_obligations")
        if not existing_obligations:
            log_error("No data available about existing obligations!")
            return False

        # Loans
        loans = existing_obligations.get("loans")
        for loan in loans:
            monthly_fixed_obligations = loan.get("monthly_emi", 0)
            
        # Credit Card monthly minimums
        credit_cards = existing_obligations.get("credit_cards")
        for credit_card in credit_cards:
            monthly_fixed_obligations += credit_card.get("monthly_min_payment", 0)

        # Other monthly expenses
        other = existing_obligations.get("other")
        for entry in other:
            if entry.get("is_monthly", False):
                monthly_fixed_obligations += entry.get("amount", 0)

        monthly_fixed_obligations += self.emi

        log_info(f"Monthly Fixed Obligations: {monthly_fixed_obligations}")

        # Next, calculate Gross Monthly Income
        gross_monthly_income = 0

        # If employed, get gross monthly salary
        employment = user.info.get("employment")
        if employment and employment.get("applicable"):
            gross_monthly_income += employment.get("monthly_gross_salary", 0)
            
        # If business, get monthly profit
        business_info = user.info.get("employment")
        if business_info and business_info.get("applicable"):
            gross_monthly_income += business_info.get("monthly_profit", 0) * business_info.get("shares_owned_fraction", 0)

        if gross_monthly_income == 0:
            log_error("No monthly income sources found!")
            return False

        log_info(f"Gross Monthly Income: {gross_monthly_income}")

        # Finally, calculate FOIR
        foir = monthly_fixed_obligations / gross_monthly_income
        
        log_info(f"FOIR: {foir}")

        return foir <= self.max_foir

    def __init__(self, ruleID: str, ruleType: str, max_foir: float, emi: float):
        super().__init__(ruleID, ruleType)
        self.max_foir = max_foir
        self.emi = emi