from adv24Tools.StringMap import StringMap
from adv24Tools.Coordinates import Coordinates


class MemoryGrid ( StringMap ):

    def __init__(self, width: int, height: int):
        map = ("." * width + '\n') * height
        super().__init__(map)


    def mark_corruption(self, coordinates: Coordinates):
        self.set_char_at(coordinates, '#')

    def is_accessible ( self, coordinates: Coordinates):
        return self.get_char_at(coordinates) == '.'