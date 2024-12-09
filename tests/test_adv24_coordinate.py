from adv24Tools.Coordinate import Coordinates

def test_subtract():
    a = Coordinates(4,5)
    b = Coordinates(6,2)
    assert a.sub(b) == Coordinates(-2,3)