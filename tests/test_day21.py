from day21.NumpadRobot import NumpadRobot
from adv24Tools.Coordinates import Coordinates


def test_numpad_robot_create ():
    testee = NumpadRobot()
    assert testee.current_position() == Coordinates (2,3)
    assert testee.current_key() == 'A'