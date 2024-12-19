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

def count_possible_solutions (pattern, available): 
    if len(pattern) == 0:
        return 1
    elif ( not is_pattern_possible(pattern, available)):
        return 0
    elif ( pattern in __seen_patterns):
        return __seen_patterns[pattern]
    
    result = 0
    for towel in available:
        if ( len(towel) <= len(pattern) and pattern[:len(towel)] == towel):
            result += count_possible_solutions(pattern[len(towel):], available)

    __seen_patterns[pattern] = result

    return result
        

def count_possible_patterns ( patterns, towels):
    result = 0
    for pattern in patterns:
        if ( is_pattern_possible(pattern, towels)):
            result += 1

    return result


__seen_patterns ={}
def count_all_solutions( patterns, towels):
    seen_patters = {}

    result = 0
    count = 0
    for pattern in patterns:
        result += count_possible_solutions(pattern, towels)
        count +=1

    return result