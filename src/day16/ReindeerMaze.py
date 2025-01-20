from adv24Tools.StringMap import StringMap
from adv24Tools.Coordinates import Coordinates

class ReindeerMaze(StringMap):

    start_position_char = "S"

    def __init__(self, map):
        super().__init__(map)

        self.start_position = self.get_coordinates_for(ReindeerMaze.start_position_char)
