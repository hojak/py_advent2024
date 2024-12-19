
from day14.Roboter import Roboter
from adv24Tools.Coordinates import Coordinates
import pytest

def test_parse_roboter_line():
    testee = Roboter.parse_line( "p=0,4 v=3,-3")

    assert testee.position == Coordinates(0,4)
    assert testee.velocity == Coordinates(3,-3)


@pytest.mark.parametrize('init_line, expected_position', [
    ("p=1,1 v=2,3", Coordinates(3,4)),
])
def test_roboter_walk(init_line, expected_position):
    testee = Roboter.parse_line(init_line)
    next_position = testee.next_position()
    assert next_position == expected_position
