from core.base_rules import HardRule, SoftRule
from core.user import User
from pydantic import BaseModel
from typing import List

class RuleSet(BaseModel):
    # 1. Define fields with type hints. 
    # Providing default empty lists [] makes it easier to initialize.
    hard_rules: List[HardRule] = []
    soft_rules: List[SoftRule] = []  # Changed to SoftRule type for accuracy

    # 2. REMOVED __init__. Pydantic handles this automatically.

    def hard_rules_satisfied(self, user: User) -> bool:
        # Note: Use 'self.hard_rules' to access the class attribute
        for rule in self.hard_rules:
            if not rule.satisfied(user):
                return False
        return True

    def soft_rules_satisfied(self, user: User) -> bool:
        # TODO: Implement scoring logic for soft rules
        return True

    def satisfied(self, user: User) -> bool:
        # Note: Use 'self' to call sibling methods
        return self.hard_rules_satisfied(user) and self.soft_rules_satisfied(user)