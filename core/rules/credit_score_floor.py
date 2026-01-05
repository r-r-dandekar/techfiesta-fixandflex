from core.base_rules import HardRule
from core.user import User
from utils.logs import log_error

class CreditScoreFloor(HardRule):

    floor : int

    def satisfied(self, user: User) -> bool:
        credit_score = user.info.get("creditProfile", {}).get("creditScore")
        if credit_score:
            return credit_score >= self.floor
        else:
            log_error("Credit score not found!")
            return False

    def __init__(self, ruleID: str, ruleType: str, floor: int):
        super().__init__(ruleID, ruleType)
        self.floor = floor