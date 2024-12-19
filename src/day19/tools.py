import re 

def parse_available_towels ( input: str )-> []:
    return re.split(', ', input)


def is_pattern_possible (pattern, available): 
    if len(pattern) == 0:
        return True
    
    for towel in available:
        if ( len(towel) <= len(pattern) and pattern[:len(towel)] == towel):
            if ( is_pattern_possible(pattern[len(towel):], available)):
                return True

    return False            
        

def count_possible_patterns ( patterns, towels):
    result = 0
    for pattern in patterns:
        if ( is_pattern_possible(pattern, towels)):
            result += 1

    return result