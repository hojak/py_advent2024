import math 


def get_string_chars ( content: str, anchor: int, offsets: list) -> str :
    result = ''
    for char_offset in offsets:
        char_index = anchor + char_offset
        if ( char_index < 0 or char_index >= len(content)):
            return ''        
        result += content[ char_index ]
    
    return result

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

        return get_string_chars(self.content,x + y*self.get_width(), offsets )
    
    
    def get_direction_delta ( self, direction: str) -> int:
        match direction:
            case 'r': return 1
            case 'l': return -1
            case 'u': return -self.get_width()
            case 'd': return self.get_width()
            case 'ru': return -self.get_width()+1
            case 'rd': return self.get_width()+1
            case 'lu': return -self.get_width()-1
            case 'ld': return self.get_width()-1
            case _: return 0

    def get_offsets_for_direction(self, direction: str, length: int) -> list:
        dirction_step_size = self.get_direction_delta(direction)

        offsets = []
        for char_number in range(length):
            char_offset = char_number*dirction_step_size
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
