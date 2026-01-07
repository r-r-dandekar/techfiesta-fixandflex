from core.rules import HardRule, SoftRule
from core.user import User

class RuleSet():
    hard_rules = []
    soft_rules = []

    def __init__(hard_rules : list[HardRule], soft_rules : list[HardRule])
        self.hard_rules = hard_rules
        self.soft_rules = soft_rules

    def hard_rules_satisfied(user : User) -> bool:
        for rule in hard_rules:
            if not rule.satisfied(user)
                return false
        return true

    def soft_rules_satisfied(user : User) -> bool:
        # TODO: Implement some sort of rule checking
        return true

    def satisfied(user : User):
        return hard_rules_satisfied(user) and soft_rules_satisfied(user)