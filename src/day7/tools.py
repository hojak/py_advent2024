import re

def is_reachable ( number: int, operants: list) -> bool : 
    if ( len ( operants ) == 1):
        return ( number == operants[0])
    
    with_plus = [operants[0] + operants[1]]+ operants[2:]
    with_multiply = [operants[0] * operants[1]]+ operants[2:]

    return is_reachable(number, with_plus) or is_reachable ( number, with_multiply )


def split_line ( line: str ):
    (number, rest) = re.split ( r':\s+', line)

    numbers = re.split ( r'\s+', rest)

    numbers = list(map(int, numbers))

    return int(number), numbers


def add_reachable_lines ( lines: str ):
    result = 0

    for line in lines.split('\n'):
        (number, operants ) = split_line ( line )
        if ( is_reachable ( number, operants)):
            result += number

    return result