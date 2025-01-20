from adv24Tools.StringMap import StringMap
from adv24Tools.Coordinates import Coordinates
class Warehouse (StringMap):
    free_space = '.'
    robot = '@'
    box = 'O'

    def __init__(self, map):
        super().__init__(map)

    def get_robot_position(self):
        return self.get_coordinates_for(Warehouse.robot)
    
    def move(self, direction):
        current_position = self.get_robot_position()

        next_position = current_position.add(Warehouse.vector_for_direction(direction))        
        
        if ( self.is_free(next_position)):
            self.move_to(next_position)
        elif ( self.is_box(next_position)):
            self.push_box(direction)

    def is_free(self, position):
        return self.get_char_at(position) == Warehouse.free_space
    
    def is_box(self, position):
        return self.get_char_at(position) == Warehouse.box


    def move_to(self, next_position):
        current_position = self.get_robot_position()
        self.set_char_at(current_position, Warehouse.free_space)
        self.set_char_at(next_position, Warehouse.robot)

    def push_box(self, direction):
        movement_vector = Warehouse.vector_for_direction(direction)
        current_position = self.get_robot_position()
        box_position = current_position.add(movement_vector)

        behind_box = box_position.add(movement_vector)

        while ( self.is_box(behind_box)):
            behind_box = behind_box.add(movement_vector)

        if ( self.is_free(behind_box)):
            self.set_char_at(current_position, Warehouse.free_space)
            self.set_char_at(box_position, Warehouse.robot)
            self.set_char_at(behind_box, Warehouse.box)


    def vector_for_direction(direction):
        vectors = {
            'v': Coordinates(0,1),
            '^': Coordinates(0,-1),
            '<': Coordinates(-1,0),
            '>': Coordinates(1,0)
        }
        return vectors[direction]
    
    def follow_plan(self, list_of_directions):
        for direction in list_of_directions:
            self.move(direction)

    def sum_of_coordinates(self):
        result = 0

        for x in range(self.get_width()):
            for y in range(self.get_height()):
                if ( self.is_box(Coordinates(x,y))):
                    result += 100 * y + x

        return result
        

    
