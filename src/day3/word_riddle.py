
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
    

