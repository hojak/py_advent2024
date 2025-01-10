from adv24Tools.Coordinates import Coordinates
from adv24Tools.StringMap import StringMap


class Robot(StringMap):

    def __init__(self, map, start_position):
        super().__init__(map)
        self.position = start_position
        self.robot_to_steer = None
        self.illegal = self.get_coordinates_for(" ")

    def get_coordinates_for(self, key):
        return self.coordinates_for_index(self.content.index(key))
    
    def current_key(self):
        return self.get_char_at(self.position)

    def current_position(self):
        return self.position
    
    def press_key ( self, key):
        return list(map(lambda path: path+'A', self.go_to_key_and_return_all_paths (key)))

    def make_final_robot_enter(self, path):
        if self.robot_to_steer == None:
            my_paths = [path]
        else:
            my_paths = self.robot_to_steer.make_final_robot_enter(path)

        result = []
        for path in my_paths:
            directions_for_this_path = ['']
            for key in path:
                next_path_steps = self.press_key(key)
                directions_for_this_path = [first_part + next_path for first_part in directions_for_this_path for next_path in next_path_steps]
            result += directions_for_this_path

        return result
    
    def shortest_length_of_sequence_for_code(self, code):
        result = -1
        for path in self.make_final_robot_enter(code):
            if result < 0 or len(path) < result:
                result = len(path)
        return result

    def go_to_key_and_return_all_paths(self, key):
        target = self.get_coordinates_for(key)
        directions = []

        if ( target.x > self.current_position().x):
            directions += [ ">" * (target.x - self.current_position().x) ]
        if ( target.x < self.current_position().x):
            directions += [ "<" * (self.current_position().x - target.x) ]
        if ( target.y < self.current_position().y):
            directions += [ "^" * (self.current_position().y - target.y) ]
        if ( target.y > self.current_position().y):
            directions += [ "v" * (target.y - self.current_position().y) ]

        old_position = self.position
        self.position = target

        if ( len(directions) <= 1 ):
            return ["".join(directions)]
        elif target.x == self.illegal.x and self.illegal.y == old_position.y:
            return [directions[1] + directions[0]]
        elif target.y == self.illegal.y and self.illegal.x == old_position.x:
            return [directions[0] + directions[1]]
        else:
            return [directions[0] + directions[1], directions[1] + directions[0]]

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
    

    
            