from core.base_rules import HardRule
from core.user import User
from utils.logs import log_error

# Fixed Obligation to Income Ratio
# a. k. a. Debt Burden
class FOIR(HardRule):

    # Expressed as a percentage e.g. 0.5
    max_foir : float

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
            monthly_emi = loan.get("monthly_emi")
            monthly_fixed_obligations += monthly_emi
            
        # Credit Card monthly minimums
        creditCards = existing_obligations.get("creditCards")
        for creditCard in creditCards:
            monthly_min_payment = creditCards.get("monthly_min_payment")
            monthly_fixed_obligations += monthly_min_payment

        # Credit Card monthly minimums
        creditCards = existing_obligations.get("creditCards")
        for creditCard in creditCards:
            monthly_min_payment = creditCards.get("monthly_min_payment")
            monthly_fixed_obligations += monthly_min_payment


        credit_score = user.info.get("creditProfile", {}).get("creditScore")
        if credit_score:
            return credit_score >= self.max_foir
        else:
            log_error("FOIR not found!")
            return False

    def __init__(self, ruleID: str, ruleType: str, max_foir: float):
        super().__init__(ruleID, ruleType)
        self.max_foir = max_foir