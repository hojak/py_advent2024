import re

class ReleaseRequirements:
    input: str
    requirements: dict
    updates: list

    def __init__(self,input: str):
        (rules_input, updates_input) = re.split (r'\n\s*\n', input)
        
        self.init_rules ( rules_input )
        self.init_updates ( updates_input )

    def init_updates ( self, updates_input):
        self.updates = []
        for update in re.split ( r'\n', updates_input):
            self.updates.append(list(map( int, update.split(','))))


    def init_rules ( self, rules_input): 
        self.requirements = {}

        for rule in re.split( r'\n', rules_input):
            (required_page, entry_page) = rule.split('|',2)
            if ( not int(entry_page) in self.requirements ):
                self.requirements[int(entry_page)] = []
            self.requirements[int(entry_page)].append ( int(required_page) )

