from adv24Tools.Coordinates import Coordinates

def test_subtract():
    a = Coordinates(4,5)
    b = Coordinates(6,2)
    assert a.sub(b) == Coordinates(-2,3)

def test_is_in_box():
    p = Coordinates(2,2)
    tl = Coordinates (-1,-11)
    br = Coordinates(3,3)
    assert p.is_in_box ( tl, br)

def test_is_not_in_box():
    p = Coordinates(-2,0)
    tl = Coordinates (-1,-11)
    br = Coordinates(3,3)
    assert not p.is_in_box ( tl, br)