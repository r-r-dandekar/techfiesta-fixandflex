# This file allows you to import members of modules in this directly simply
# E.g. from core.rules import CreditScoreFloor
# Where CreditScoreFloor is defined in core/rules/credit_score_floor.py

import pkgutil
import importlib
import inspect
from core.base_rules import Rule # Import the base to identify children

# This list will help you see what was loaded
__all__ = []

for loader, module_name, is_pkg in pkgutil.iter_modules(__path__):
    try:
        module = importlib.import_module(f".{module_name}", package=__name__)
        
        for name, obj in inspect.getmembers(module, inspect.isclass):
            # 1. Is it defined in that file? 
            # 2. Is it a subclass of Rule?
            # 3. Is it NOT the Rule class itself?
            if obj.__module__ == module.__name__ and issubclass(obj, Rule):
                globals()[name] = obj
                __all__.append(name)
    except Exception as e:
        print(f"Failed to load rule module {module_name}: {e}")