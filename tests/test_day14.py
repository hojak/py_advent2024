
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
def test_roboter_step(init_line, expected_position):
    max_size = Coordinates(10,10)

    testee = Roboter.parse_line(init_line)
    next_position = testee.next_position(max_size)
    assert next_position == expected_position


@pytest.mark.parametrize('init_line, steps, expected_position', [
    ("p=2,4 v=2,-3", 0, Coordinates(2,4)),
    ("p=2,4 v=2,-3", 1, Coordinates(4,1)),
    ("p=2,4 v=2,-3", 2, Coordinates(6,5)),
    ("p=2,4 v=2,-3", 3, Coordinates(8,2)),
    ("p=2,4 v=2,-3", 4, Coordinates(10,6)),
    ("p=2,4 v=2,-3", 5, Coordinates(1,3)),
])
def test_roboter_steps(init_line, steps, expected_position):
    max_size = Coordinates(11,7)

    testee = Roboter.parse_line(init_line)
    testee.walk ( steps, max_size )

    assert testee.position == expected_position

def test_roboter_walk():
    max_size = Coordinates(150,150)
    testee = Roboter.parse_line("p=2,4 v=1,2")
    testee.walk ( 100, max_size)
    assert testee.position == Coordinates ( 102, 54)
