import re, math

def get_middle_number ( list: list ) -> int:
    index = math.floor(len(list) / 2)
    return list[index]

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

    def is_valid (self, update: list) -> bool: 
        seen = []
        for page in reversed(update):
            if page in self.requirements:
                for required_page in self.requirements[page]:
                    if required_page in seen:
                        return False
            seen.append(page)
        return True

    def get_sum_for_valid_updates(self) -> int:
        result = 0
        for update in self.updates:
            if ( self.is_valid(update)):
                result += get_middle_number(update)
        return result
    
    def get_fix(self, update: list) -> list:
        work = update

        # assumption: every update sequence is fixable
        # otherwise we'd run into an endless loop here
        # indicator: a rule is used twice to derive a fix
        while not self.is_valid(work):
            work = self.fix_step( work )

        return work
    
    def fix_step (self, work: list) -> list:
        seen = []

        for index in reversed(range(len(work))):
            page = work[index]

            if page in self.requirements:
                for required_page in self.requirements[page]:
                    try:
                        problem_index = seen.index (required_page)
                        result = work[:index] + seen[:problem_index+1] + [page] + seen[problem_index+1:]
                        return result
                    except:
                        pass

            seen = [page] + seen

        raise Exception("could not find fix")
