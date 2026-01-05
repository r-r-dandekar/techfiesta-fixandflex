from core.base_rules import HardRule
from core.user import User
from utils.logs import log_error

class IncomeFloor(HardRule):
    """Minimum net earnings to qualify."""
    min_net_income: float

    def __init__(self, ruleID: str, ruleType: str, min_net_income: float = 25000):
        super().__init__(ruleID, ruleType)
        self.min_net_income = min_net_income

    def satisfied(self, user: User) -> bool:
        net_income = user.info.get("employment", {}).get("monthly_net_salary")
        if net_income is not None:
            return net_income >= self.min_net_income
        log_error("Monthly net salary not found")
        return False