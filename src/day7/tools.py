
def is_reachable ( number: int, operants: list) -> bool : 
    if ( len ( operants ) == 1):
        return ( number == operants[0])
    
    return False
