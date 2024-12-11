import math

def blink ( list_of_stones : list ) -> list :
    result = []
    for stone in list_of_stones:
        if stone == 0:
            result.append(1)
        else:
            result.append(stone)

    return result