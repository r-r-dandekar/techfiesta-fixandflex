from core.rules.rule import Rule
from core.user import User

class HardRule(Rule):

    def satisifed(user: User) -> bool:
        pass

    def __init__(self, ruleID: str, ruleType: str):
        super().__init__(ruleID, ruleType)