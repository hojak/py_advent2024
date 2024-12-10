import math

from adv24Tools.Coordinate import Coordinates 
from adv24Tools.StringMap import StringMap

class WordRiddle (StringMap):
    def __init__(self, init_str):
        super().__init__(init_str)

    
    def get_chars_in_direction (self,x: int,y: int,direction:str,length: int) -> str:
        offsets = self.get_offsets_for_direction(direction, length)

        return self.get_string_chars(Coordinates(x,y), offsets )
    
    
    def get_direction_delta ( self, direction: str):
        match direction:
            case 'r': return Coordinates(1,0)
            case 'l': return Coordinates(-1,0)
            case 'u': return Coordinates(0,-1)
            case 'd': return Coordinates(0,1)
            case 'ru': return Coordinates(1,-1)
            case 'rd': return Coordinates(1,1)
            case 'lu': return Coordinates(-1,-1)
            case 'ld': return Coordinates(-1,1)
            case _: return Coordinates(0,0)

    def get_offsets_for_direction(self, direction: str, length: int) -> list:
        direction_step = self.get_direction_delta(direction)

        offsets = []
        for char_number in range(length):
            char_offset = direction_step.mul(char_number)
            offsets.append(char_offset)
        return offsets


    def number_of_occurences (self, look_for: str ) -> int :
        result = 0
        directions = ['r', 'l', 'u', 'd', 'ru', 'lu', 'rd', 'ld']
        for x in range(self.get_width()): 
            for y in range (self.get_height()):
                for direction in directions:
                    if ( self.get_chars_in_direction(x, y, direction, len(look_for)) == look_for ):
                        result += 1
        return result

    def get_string_chars ( self, anchor: Coordinates, offsets: list) -> str :
        result = ''
        for char_offset in offsets:
            char_coordinates = anchor.add(char_offset)
            if ( not self.is_within_bounds(char_coordinates)):
                return ''
            char_index = char_coordinates.get_index(self.width)
            result += self.content[ char_index ]
        
        return result

    def is_within_bounds ( self, c ) -> bool: 
        return c.x >= 0 and c.y >= 0 and c.x < self.width and c.y < self.height
    
    def count_x_of_mas(self) -> int: 
        offsets = [Coordinates(0,0),Coordinates(-1,-1),Coordinates(1,-1),Coordinates(1,1),Coordinates(-1,1)]
        possible_versions = ['AMMSS', 'AMSSM', 'ASSMM', 'ASMMS']

        found = 0

        for x in range(1,self.get_width()-1): 
            for y in range (1,self.get_height()-1):
                check = self.get_string_chars(Coordinates(x,y), offsets)
                if check in possible_versions:
                    found += 1

        return found