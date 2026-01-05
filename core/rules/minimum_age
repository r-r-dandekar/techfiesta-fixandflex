from core.base_rules import HardRule
from core.user import User
from utils.logs import log_error

class MinimumAge(HardRule):
    """User must be an adult to take a loan."""
    min_age: int

    def __init__(self, ruleID: str, ruleType: str, min_age: int = 21):
        super().__init__(ruleID, ruleType)
        self.min_age = min_age

    def satisfied(self, user: User) -> bool:
        age = user.info.get("personal_info", {}).get("age")
        if age is not None:
            return age >= self.min_age
        log_error("Age not found in personal_info")
        return False