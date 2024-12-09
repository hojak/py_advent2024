from adv24Tools.Coordinate import Coordinate

def test_subtract():
    a = Coordinate(4,5)
    b = Coordinate(6,2)
    assert a.sub(b) == Coordinate(-2,3)