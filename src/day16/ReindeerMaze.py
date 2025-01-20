from adv24Tools.StringMap import StringMap
from adv24Tools.Coordinates import Coordinates

class ReindeerMaze(StringMap):

    def start_position(self):
        return Coordinates(1,1)