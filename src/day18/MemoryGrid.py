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
        
        step = 0

        queue = [(from_position, 0)]

        while len(queue) > 0:
            (current_position, steps_till_here) = queue.pop(0) # shift

            if ( not self.is_accessible ( current_position)):
                continue

            if ( current_position == to_position):
                self.content = self.content.replace('O', '.')
                return steps_till_here

            self.set_char_at(current_position, 'O')

            for direction in directions:
                next = current_position.add(direction)
                if ( self.is_accessible(next)):
                    queue.append( (next, steps_till_here+1))
                
        return -1

