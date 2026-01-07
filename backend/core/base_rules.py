from core.user import User

class Rule:
    ruleID : str
    ruleType : str

    def __init__(self, ruleID: str, ruleType: str):
        self.ruleID = ruleID
        self.ruleType = ruleType

class HardRule(Rule):

    def satisfied(self, user: User) -> bool:
        pass

    def __init__(self, ruleID: str, ruleType: str):
        super().__init__(ruleID, ruleType)

class SoftRule(Rule):

    def rate_impact(self, user: User) -> float:
        pass

    def tenure_impact(self, user: User) -> float:
        pass
        
    def __init__(self, ruleID: str, ruleType: str):
        super().__init__(ruleID, ruleType)