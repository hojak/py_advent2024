from adv24Tools.Coordinate import Coordinates


import math


class StringMap:
    content: str
    width: int
    heigth: int

    def __init__(self, map: str):
        self.content = map
        self.init_map (map)

    def init_map(self, init_str):
        self.content = init_str.replace('\n', '')
        found = init_str.find('\n')
        if (found >= 0):
            self.width = found
        else:
            self.width = len(init_str)
        self.height = math.ceil(len(self.content) / self.width)

        if ( self.width * self.height != len(self.content)):
            raise Exception ( "illegal length of map definition")

    def coordinates_for_index ( self, index ) -> Coordinates:
        return Coordinates( index % self.width, math.floor(index / self.width) )

    def index_for_coordinates ( self, coordinates: Coordinates) -> int:
        return coordinates.x + coordinates.y * self.width
    
    def get_width(self) -> int:
        return self.width
    
    def get_height(self) -> int:
        return self.height
    
    def is_within_bounds ( self, c : Coordinates ) -> bool: 
        return c.x >= 0 and c.y >= 0 and c.x < self.width and c.y < self.height
