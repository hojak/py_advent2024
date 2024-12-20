
class Coordinates:
    x: int
    y: int

    def __init__(self,x: int, y:int):
        self.x = x
        self.y = y

    def get_index( self, width ) -> int:
        return width*self.y + self.x

    def add (self, a):
        return Coordinates(self.x + a.x, self.y + a.y)

    def mul (self, m: int):
        return Coordinates(self.x*m, self.y*m)
    
    def sub ( self, a):
        return Coordinates(self.x - a.x, self.y - a.y)

    def __str__(self) -> str:
        return "("+str(self.x) + "/" + str(self.y) + ")"
    
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y
    
    def is_in_box ( self, top_left, bottom_right):
        return self.x >= top_left.x \
            and self.x <= bottom_right.x \
            and self.y >= top_left.y \
            and self.y <= bottom_right.y
    



directions = [
    Coordinates(1,0),
    Coordinates(0,1),
    Coordinates(-1,0),
    Coordinates(0,-1),
]
