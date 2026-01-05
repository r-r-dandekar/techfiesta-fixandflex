from core.base_rules import HardRule
from core.user import User
from utils.logs import log_error

class CreditScoreFloor(HardRule):

    min_score : int

    def satisfied(self, user: User) -> bool:
        credit_score = user.info.get("credit_profile", {}).get("credit_score")
        if credit_score:
            return credit_score >= self.min_score
        else:
            log_error("Credit score not found!")
            return False

    def __init__(self, ruleID: str, ruleType: str, min_score: int):
        super().__init__(ruleID, ruleType)
        self.min_score = min_score