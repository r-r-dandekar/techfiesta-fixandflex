from core.base_rules import HardRule
from core.user import User
from utils.logs import log_error

class DefaultHistory(HardRule):
    """No active defaults or bankruptcy allowed."""
    def satisfied(self, user: User) -> bool:
        profile = user.info.get("credit_profile", {})
        has_default = profile.get("has_default_history", True)
        has_bankruptcy = profile.get("bankruptcy_history", True)
        
        # Returns True only if both are False
        return (not has_default) and (not has_bankruptcy)