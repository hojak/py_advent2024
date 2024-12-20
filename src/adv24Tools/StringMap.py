from adv24Tools.Coordinates import Coordinates


import math
import re


class StringMap:
    CHAR_FREE = '.'
    CHAR_BLOCK = '#'

    # instance attributes
    # content: str
    # width: int
    # heigth: int

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

    def index_for_xy ( self, x: int, y: int) -> int:
        return self.index_for_coordinates ( Coordinates(x,y))
    
    def get_width(self) -> int:
        return self.width
    
    def get_height(self) -> int:
        return self.height
    
    def is_within_bounds ( self, c : Coordinates ) -> bool: 
        return c.x >= 0 and c.y >= 0 and c.x < self.width and c.y < self.height
    
    def is_out_of_bounds (self, x, y ) -> bool :
        return not self.is_within_bounds(Coordinates(x,y))
    
    def add_line_breaks ( self, content ): 
        return re.sub('(.{'+str(self.get_width())+'})',r'\1\n', content)[:-1]
    
    def get_char_at( self, location: Coordinates ) -> str : 
        if not self.is_within_bounds(location):
            return ''
        
        return self.content[self.index_for_coordinates(location)]
    
    def set_char_at ( self, location: Coordinates, new_char: str):
        index = self.index_for_coordinates(location)
        self.content = self.content[:index] + new_char + self.content[index+1:]

    def __str__(self):
        return self.add_line_breaks(self.content)

