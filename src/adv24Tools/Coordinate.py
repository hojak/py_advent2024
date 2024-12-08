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