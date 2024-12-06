import math
import re

class LabMap:

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

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
