from core.rules.ruleset import RuleSet
from pydantic import BaseModel

class LoanScheme(BaseModel):
    loan_id : str
    rule_set : RuleSet
    name : str
    description : str

    def load_from_db(self):
        pass