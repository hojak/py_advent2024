from adv24Tools.StringMap import StringMap
from adv24Tools.Coordinates import Coordinates
class Warehouse (StringMap):

    def __init__(self, map):
        super().__init__(map)

    def get_coordinates_for(self, key):
        return self.coordinates_for_index(self.content.index(key))
    
    def get_robot_position(self):
        return self.get_coordinates_for('@')
    
    def move(self, direction):
        current_position = self.get_robot_position()

        next_position = current_position.add(Coordinates(1,0))        
        
        self.set_char_at(current_position, '.')
        self.set_char_at(next_position, '@')
        

    
