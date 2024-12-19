
from day14.Roboter import Roboter
from adv24Tools.Coordinates import Coordinates

def test_parse_roboter_line():
    testee = Roboter.parse_line( "p=0,4 v=3,-3")

    assert testee.position == Coordinates(0,4)
    assert testee.velocity == Coordinates(3,-3)