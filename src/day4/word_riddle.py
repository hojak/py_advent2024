import math 

class Coordinate:
    x: int
    y: int

    def __init__(self,x: int, y:int):
        self.x = x
        self.y = y

    def get_index( self, width ) -> int:
        return width*self.y + self.x
    
    def add (self, a):
        return Coordinate(self.x + a.x, self.y + a.y)
    
    def mul (self, m: int):
        return Coordinate(self.x*m, self.y*m)


class WordRiddle:
    content: str
    width: int
    height: int

    def __init__(self, init_str):
        self.content = init_str.replace('\n', '')
        found = init_str.find('\n')
        if (found >= 0):
            self.width = found
        else:
            self.width = len(init_str)
        self.height = math.ceil(len(self.content) / self.width)

    def get_width(self) -> int:
        return self.width
    
    def get_height(self) -> int:
        return self.height
    
    def get_chars_in_direction (self,x: int,y: int,direction:str,length: int) -> str:
        offsets = self.get_offsets_for_direction(direction, length)

        return self.get_string_chars(Coordinate(x,y), offsets )
    
    
    def get_direction_delta ( self, direction: str):
        match direction:
            case 'r': return Coordinate(1,0)
            case 'l': return Coordinate(-1,0)
            case 'u': return Coordinate(0,-1)
            case 'd': return Coordinate(0,1)
            case 'ru': return Coordinate(1,-1)
            case 'rd': return Coordinate(1,1)
            case 'lu': return Coordinate(-1,-1)
            case 'ld': return Coordinate(-1,1)
            case _: return Coordinate(0,0)

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

    def get_string_chars ( self, anchor: Coordinate, offsets: list) -> str :
        result = ''
        for char_offset in offsets:
            char_coordinates = anchor.add(char_offset)
            if ( not self.is_within_bounds ( char_coordinates)):
                return ''
            char_index = char_coordinates.get_index(self.width)
            result += self.content[ char_index ]
        
        return result

    def is_within_bounds ( self, c ) -> bool: 
        return c.x>=0 and c.y >= 0 and c.x < self.width and c.y < self.height