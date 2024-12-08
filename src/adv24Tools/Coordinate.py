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

    def __str__(self) -> str:
        return "("+str(self.x) + "/" + str(self.y) + ")"