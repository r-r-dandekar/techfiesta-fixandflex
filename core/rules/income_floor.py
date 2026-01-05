from core.base_rules import HardRule
from core.user import User
from utils.logs import log_error, log_info

class IncomeFloor(HardRule):
    """
    Minimum earnings to qualify for the specific product tier.
    Logic: NetIncome >= Rule.MinIncome
    Considers both Salaried Net Salary and Business Profits.
    """
    min_income: float

    def __init__(self, ruleID: str, ruleType: str, min_income: float = 25000):
        super().__init__(ruleID, ruleType)
        self.min_income = min_income

    def satisfied(self, user: User) -> bool:
        # Calculate Total Monthly Net Income based on the FOIR logic style
        total_net_income = 0

        # 1. Salaried Income
        employment = user.info.get("employment")
        if employment and employment.get("applicable"):
            # Using net salary for the 'Floor' check as per your requirement logic
            total_net_income += employment.get("monthly_net_salary", 0)
            # Including other income sources if present
            total_net_income += employment.get("other_monthly_income", 0)

        # 2. Business Income
        business_info = user.info.get("business_info")
        if business_info and business_info.get("applicable"):
            profit = business_info.get("monthly_profit", 0) or 0
            fraction = business_info.get("shares_owned_fraction", 0) or 0
            total_net_income += (profit * fraction)

        if total_net_income == 0:
            log_error("No income sources found for IncomeFloor check!")
            return False

        log_info(f"Total calculated Net Income: {total_net_income}")
        
        return total_net_income >= self.min_income