import math

def blink ( list_of_stones : list ) -> list :
    result = []
    for stone in list_of_stones:
        stone_as_string = str(stone)
        if stone == 0:
            result.append(1)
        elif len(stone_as_string) % 2 == 0:
            half_length = math.floor(len(stone_as_string) / 2)
            result.append ( int(stone_as_string[:half_length]))
            result.append ( int(stone_as_string[half_length:]))
        else:
            result.append(stone)

    return result