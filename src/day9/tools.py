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


def move_blocks (input: list) -> list :
    result = input

    id_to_move =  result[len(result)-1][1]

    while ( id_to_move > 0):
        index_to_move = find_id ( id_to_move, result)
        item_to_move = result[index_to_move]

        target_index = find_free_space ( result, result[index_to_move][0])

        if (target_index >= 0 and target_index < index_to_move):
            insert = [item_to_move]
            if ( item_to_move[0]< result[target_index][0]):
                insert.append ( [result[target_index][0] - item_to_move[0], '.'] )

            result = result[:target_index] + insert + result[target_index+1:index_to_move] + [[item_to_move[0],'.']] + result[index_to_move+1:]

        id_to_move -= 1


    return combine_free_spaces (result)


def find_id(id, blocks):
    for index in range(len(blocks)):
        if ( blocks[index][1] == id):
            return index
        

def find_free_space ( blocks, size ):
    result = 0
    
    for index in range ( len ( blocks )):
        if ( blocks[index][1] == '.' and blocks[index][0] >= size):
            return index
        
    return -1


def combine_free_spaces ( blocks ) :
    index = 0
    while index < len(blocks)-1:
        while index+1 < len(blocks) and blocks[index][1] == '.' and blocks[index+1][1] == '.':
            blocks = blocks[:index] + [[blocks[index][0] + blocks[index+1][0], '.']] + blocks[index+2:]
        index += 1
        
    return blocks



def checksum_for_blocks ( blocks ): 
    result = 0
    start_index = 0

    for block in blocks:
        if ( block [1] != '.'):
            result += get_block_value ( block, start_index)
        start_index += block[0]

    return result

def get_block_value ( block, start_index):
    result = 0
    for i in range ( block[0]):
        result += (i + start_index) * block[1]
    return result