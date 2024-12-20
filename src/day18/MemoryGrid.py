from adv24Tools.StringMap import StringMap
from adv24Tools.Coordinates import Coordinates, directions


def parse_coordinates ( input: str) -> [Coordinates] :
    result = []
    for line in input.splitlines():
        (x,y) = line.split(',')
        result.append(Coordinates(int(x),int(y)))
    return result


class MemoryGrid ( StringMap ):

    def __init__(self, width: int, height: int):
        map = ("." * width + '\n') * height
        super().__init__(map)


    def mark_corruption(self, coordinates: Coordinates):
        self.set_char_at(coordinates, '#')

    def is_accessible ( self, coordinates: Coordinates):
        return self.get_char_at(coordinates) == '.'
    
    def steps_to_exit ( self, from_position, to_position ) -> int :
        if ( not self.is_accessible(from_position)):
            return -1
        
        if ( from_position == to_position ):
            return 0
        
        self.set_char_at(from_position, '#')

        result = -1
        for direction in directions:
            next = from_position.add(direction)
            if ( self.is_accessible(next)):
                steps_for_this_direction = self.steps_to_exit(next, to_position)
                if ( steps_for_this_direction >= 0 and ( result == -1 or result > steps_for_this_direction)):
                    result = steps_for_this_direction + 1

        self.set_char_at(from_position, '.')

        return result