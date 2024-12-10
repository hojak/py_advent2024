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

    print (result)

    while ( id_to_move > 0):
        index_to_move = find_id ( id_to_move, result)
        item_to_move = result[index_to_move]

        print ( "found id " + str(id_to_move) + " at " + str( index_to_move) + " --> " + str(result[index_to_move]))

        target_index = find_free_space ( result, result[index_to_move][0])

        if (target_index >= 0 and target_index < index_to_move):
            insert = [item_to_move]
            if ( item_to_move[0]< result[target_index][0]):
                insert.append ( [result[target_index][0] - item_to_move[0], '.'] )

            result = result[:target_index] + insert + result[target_index+1:index_to_move] + [[item_to_move[0],'.']] + result[index_to_move+1:]

            print (result)

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
    for index in range(len(blocks) -1):
        if( blocks[index][1] == '.' and blocks[index+1][1] == '.'):
            return combine_free_spaces ( blocks[:index] + [[blocks[index][0] + blocks[index+1][0], '.']] + blocks[index+2:] )
        
    return blocks

