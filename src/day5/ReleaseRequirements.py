import re

class ReleaseRequirements:
    input: str

    def __init__(self,input: str):
        (rules_input, updates_input) = re.split (r'\n\s*\n', input)
        self.rules = re.split( r'\n', rules_input)
        self.updates = re.split ( r'\n', updates_input)


    def get_rules(self) -> list:
        return self.rules
    
    def get_updates(self) -> list:
        return self.updates
