class Rule:
    ruleID : str
    ruleType : str

    def __init__(self, ruleID: str, ruleType: str):
        self.ruleID = ruleID
        self.ruleType = ruleType