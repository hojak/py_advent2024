import re 

def parse_available_towels ( input: str )-> []:
    return re.split(', ', input)