
def is_reachable ( number: int, operants: list) -> bool : 
    if ( len ( operants ) == 1):
        return ( number == operants[0])
    
    with_plus = [operants[0] + operants[1]]+ operants[2:]
    with_multiply = [operants[0] * operants[1]]+ operants[2:]

    return is_reachable(number, with_plus) or is_reachable ( number, with_multiply )
