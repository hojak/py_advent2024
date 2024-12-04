
def get_every_x_char ( content: str, start: int, offset: int, length: int) -> str :
    result = ''
    for char_number in range(length):
        result += content[ start + char_number*offset ]
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
        self.height = len(self.content) / self.width

    def get_width(self) -> int:
        return self.width
    
    def get_height(self) -> int:
        return self.height
    
    def get_chars_in_direction (self,x: int,y: int,direction:str,length: int) -> str:
        if ( not self.stays_within_dimensions (x,y,direction, length)):
            return ''
        
        offset = self.get_direction_offset(direction)

        return get_every_x_char(self.content, x + y*self.get_width(), offset, length )
    
    def stays_within_dimensions ( self, x, y, direction, length) -> bool:
        if ( not self.is_in_grid(x,y)):
            return False
        if ( 'r' in direction and x+length-1 >= self.width ):
            return False
        if ( 'l' in direction and length > x+1):
            return False
        if ( 'd' in direction and y+length-1 >= self.height):
            return False
        if ( 'u' in direction and length > y+1):
            return False
        
        return True


    def is_in_grid (self, x: int, y: int) -> bool:
        return x >= 0 and y >= 0 and x < self.width and y < self.height
    
    def get_direction_offset ( self, direction: str) -> int:
        match direction:
            case 'r': return 1
            case 'l': return -1
            case 'u': return -self.get_width()
            case 'd': return self.get_width()
            case 'ru': return -self.get_width()+1
            case 'rd': return self.get_width()+1
            case 'lu': return self.get_width()-1
            case 'ld': return self.get_width()-1
            case _: return 0



