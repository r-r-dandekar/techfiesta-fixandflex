from core.rules.rules import Rule

class SoftRule(Rule):

    def rate_impact() -> float:
        pass

    def tenure_impact() -> float:
        pass
        
    def __init__(self, ruleID: str, ruleType: str):
        super().__init__(ruleID, ruleType)