from adv24Tools.StringMap import StringMap
from adv24Tools.Coordinates import Coordinates
class Warehouse (StringMap):
    free_space = '.'
    robot = '@'

    def __init__(self, map):
        super().__init__(map)

    def get_coordinates_for(self, key):
        return self.coordinates_for_index(self.content.index(key))
    
    def get_robot_position(self):
        return self.get_coordinates_for(Warehouse.robot)
    
    def move(self, direction):
        current_position = self.get_robot_position()

        next_position = current_position.add(Warehouse.vector_for_direction(direction))        
        
        if ( self.get_char_at(next_position) == Warehouse.free_space):
            self.set_char_at(current_position, Warehouse.free_space)
            self.set_char_at(next_position, Warehouse.robot)

    def vector_for_direction(direction):
        vectors = {
            'v': Coordinates(0,1),
            '^': Coordinates(0,-1),
            '<': Coordinates(-1,0),
            '>': Coordinates(1,0)
        }
        return vectors[direction]
        

    
