def expand ( input: str) -> list:
    result = []
    next_is_block = True
    block_number = 0

    for char in input: 
        if ( next_is_block ):
            for i in range ( int(char)):
                result.append ( block_number )
            block_number += 1
        else:
            for i in range ( int(char)):
                result.append('.')
        
        next_is_block = not next_is_block

    return result