from adv24Tools.StringMap import StringMap
class Warehouse (StringMap):

    def __init__(self, map):
        super().__init__(map)
        self.robot_position = self.get_coordinates_for('@')

    def get_coordinates_for(self, key):
        return self.coordinates_for_index(self.content.index(key))
    
    def get_robot_position(self):
        return self.robot_position

    
