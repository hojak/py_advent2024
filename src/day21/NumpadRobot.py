from adv24Tools.Coordinates import Coordinates
from adv24Tools.StringMap import StringMap

class NumpadRobot (StringMap):

    def __init__(self):
        super().__init__("789\n456\n123\n 0A")
        self.position = Coordinates(2,3)
        
    def current_position(self):
        return self.position
    
    def current_key(self):
        return self.get_char_at(self.position)
    
    def get_coordinates_for(self, key):
        return self.coordinates_for_index(self.content.index(key))
    