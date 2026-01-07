from core.base_rules import HardRule
from core.user import User
from utils.logs import log_error

class CreditScoreFloor(HardRule):
    min_score: int
    rule_type: str = "credit_score_floor"

    def satisfied(self, user: User) -> bool:
        credit_score = user.info.get("credit_profile", {}).get("credit_score")
        
        if credit_score is not None:
            return credit_score >= self.min_score
        
        log_error(f"Rule {self.rule_id}: Credit score not found for user!")
        return False