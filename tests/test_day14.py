
from day14.Roboter import Roboter
from adv24Tools.Coordinates import Coordinates
import pytest

def test_parse_roboter_line():
    testee = Roboter.parse_line( "p=0,4 v=3,-3")

    assert testee.position == Coordinates(0,4)
    assert testee.velocity == Coordinates(3,-3)


@pytest.mark.parametrize('init_line, expected_position', [
    ("p=1,1 v=2,3", Coordinates(3,4)),
    ("p=1,2 v=10,10", Coordinates(1,2)),
])
def test_roboter_walk(init_line, expected_position):
    max_size = Coordinates(10,10)

    testee = Roboter.parse_line(init_line)
    next_position = testee.next_position(max_size)
    assert next_position == expected_position
