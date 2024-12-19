import re 

def parse_available_towels ( input: str )-> []:
    return re.split(', ', input)


def is_pattern_possible (pattern, available): 
    return count_possible_solutions(pattern, available) > 0          

def count_possible_solutions (pattern, available): 
    if len(pattern) == 0:
        return 1
    
    result = 0
    for towel in available:
        if ( len(towel) <= len(pattern) and pattern[:len(towel)] == towel):
            result += count_possible_solutions(pattern[len(towel):], available)

    return result
        

def count_possible_patterns ( patterns, towels):
    result = 0
    for pattern in patterns:
        if ( is_pattern_possible(pattern, towels)):
            result += 1

    return result