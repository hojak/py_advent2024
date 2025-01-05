from adv24Tools.Coordinates import Coordinates
from adv24Tools.StringMap import StringMap


class Robot(StringMap):

    def __init__(self, map, start_position):
        super().__init__(map)
        self.position = start_position
        self.robot_to_steer = None

    def get_coordinates_for(self, key):
        return self.coordinates_for_index(self.content.index(key))
    
    def current_key(self):
        return self.get_char_at(self.position)

    def current_position(self):
        return self.position
    
    def press_key ( self, key):
        return self.go_to_key(key) + "A"

    def make_final_robot_enter(self, sequence):
        if self.robot_to_steer == None:
            my_sequence = sequence
        else:
            my_sequence = self.robot_to_steer.make_final_robot_enter(sequence)
        
        print ("sequence: "+sequence + " -> " + my_sequence)

        result = ''
        for key in my_sequence:
            result += self.press_key(key)
        return result
    
    def length_of_sequence_for_code(self, code):
        return len ( self.make_final_robot_enter(code))

class NumpadRobot (Robot):
    def __init__(self):
        super().__init__("789\n456\n123\n 0A", Coordinates(2,3))

    def go_to_key(self, key):
        target = self.get_coordinates_for(key)
        path = ''

        if ( target.x > self.current_position().x):
            path += ">" * (target.x - self.current_position().x)

        if ( target.y < self.current_position().y):
            path += "^" * (self.current_position().y - target.y)

        if ( target.x < self.current_position().x):
            path += "<" * (self.current_position().x - target.x)

        if ( target.y > self.current_position().y):
            path += "v" * (target.y - self.current_position().y)

        self.position = target

        return path

        
class DirectionpadRobot (Robot):
    def __init__(self):
        super().__init__(" ^A\n<v>", Coordinates(2,0))

    def go_to_key(self, key):
        target = self.get_coordinates_for(key)
        path = ''

        if ( target.y > self.current_position().y):
            path += "v" * (target.y - self.current_position().y)

        if ( target.x > self.current_position().x):
            path += ">" * (target.x - self.current_position().x)

        if ( target.y < self.current_position().y):
            path += "^" * (self.current_position().y - target.y)

        if ( target.x < self.current_position().x):
            path += "<" * (self.current_position().x - target.x)


        self.position = target

        return path     
    

    def assign_robot_to_steer(self, robot: Robot):
        self.robot_to_steer = robot
    
    def make_assigned_press_key(self, target_key):
        path_of_assigned = self.robot_to_steer.go_to_key(target_key) + "A"

        my_path = ""
        for key in path_of_assigned:
            my_path += self.press_key(key)

        return my_path
    
    def make_assigned_press_sequence(self, sequence):
        result = ''
        for key in sequence:
            result += self.make_assigned_press_key(key)

        return result

    
            