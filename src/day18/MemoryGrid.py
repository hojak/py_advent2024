from adv24Tools.StringMap import StringMap
from adv24Tools.Coordinates import Coordinates, directions
import math


def parse_coordinates ( input: str) -> [Coordinates] :
    result = []
    for line in input.splitlines():
        (x,y) = line.split(',')
        result.append(Coordinates(int(x),int(y)))
    return result


class MemoryGrid ( StringMap ):
    def __init__(self, width: int, height: int):
        map = (StringMap.CHAR_FREE * width + '\n') * height
        super().__init__(map)

    def mark_corruption(self, coordinates: Coordinates):
        self.set_char_at(coordinates, StringMap.CHAR_BLOCK)


    def find_blocking_coordinates (width, height, list_of_coordinates):
        lower_end = 0
        upper_end = len(list_of_coordinates)-1

        while lower_end +1 != upper_end:
            check = math.floor((upper_end+lower_end) / 2)
            print ( str ( lower_end) + " - " + str(upper_end) + " -> " + str(check) )

            grid = MemoryGrid.initialize_grid(width, height, list_of_coordinates[:check+1])
            if ( grid.length_of_path(Coordinates(0,0), Coordinates(width-1, height-1)) >= 0):
                lower_end = check
            else:
                upper_end = check

        return list_of_coordinates[upper_end]
    

    def initialize_grid ( width, height, list_of_coordinates):
        result = MemoryGrid(width, height)
        for coordinates in list_of_coordinates:
            result.mark_corruption(coordinates)
        return result
