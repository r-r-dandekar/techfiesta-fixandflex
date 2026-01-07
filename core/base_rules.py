from core.user import User
from pydantic import BaseModel
from typing import Any

class Rule(BaseModel):
    rule_id: str
    rule_type: str

class HardRule(Rule):
    def satisfied(self, user: Any) -> bool:
        pass
        
class SoftRule(Rule):

    def rate_impact(self, user: User) -> float:
        pass

    def tenure_impact(self, user: User) -> float:
        pass