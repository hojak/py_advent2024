from adv24Tools.StringMap import StringMap
from adv24Tools.Coordinates import Coordinates
from day25.Keyhole import Keyhole

class Key:

    def __init__(self, definition: str):
        map = StringMap (definition)
        self.heights = [0,0,0,0,0]

        for column in range(len(self.heights)):
            height = 0
            while map.get_char_at(Coordinates(column,5-height)) == '#':
                height += 1
            self.heights[column] = height
        

    def get_height(self, column: int) -> int:
        return self.heights[column]
    
    def fits_into(self, keyhole: Keyhole)->bool:
        for column in range (len(self.heights)):
            if ( self.get_height(column) + keyhole.get_height(column)) > 5:
                return False
        return True