from adv24Tools.StringMap import StringMap
from adv24Tools.Coordinates import Coordinates

class ReindeerMaze(StringMap):

    start_position_char = "S"
    end_position_char = "E"

    def __init__(self, map):
        super().__init__(map)

        self.start_position = self.get_coordinates_for(ReindeerMaze.start_position_char)
        self.end_position = self.get_coordinates_for(ReindeerMaze.end_position_char)
