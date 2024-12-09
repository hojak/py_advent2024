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


def compact ( input: list) -> list :
    result = input

    next_free = 0
    while ( input[next_free ] != '.' and next_free < len(input)):
        next_free+=1

    index_to_move = len(input)-1
    while ( input[index_to_move] == '.' and index_to_move > 0):
        index_to_move -= 1

    while next_free < index_to_move:
        result[next_free] = input[index_to_move]
        result[index_to_move] = '.'

        while ( input[next_free ] != '.' and next_free < len(input)):
            next_free+=1
        
        while ( input[index_to_move] == '.' and index_to_move > 0):
            index_to_move -= 1

    return result


def checksum ( input : list) -> int :
    result = 0
    for index in range ( len ( input )):
        if ( input[index] != '.'):
            result += index * input[index]

    return result

def expand_to_blocks ( input: str) -> list:
    result = []
    next_is_block = True
    block_number = 0

    for char in input: 
        if ( next_is_block ):
            result.append ( [int(char), block_number])
            block_number += 1
        elif char != '0':
            result.append ( [int(char), '.'])
        
        next_is_block = not next_is_block

    return result