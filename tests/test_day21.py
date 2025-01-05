from day21.NumpadRobot import NumpadRobot, DirectionpadRobot
from adv24Tools.Coordinates import Coordinates

import pytest

def test_numpad_robot_create ():
    testee = NumpadRobot()
    assert testee.current_position() == Coordinates (2,3)
    assert testee.current_key() == 'A'


def test_robot_get_coordinates_of_key():
    testee = NumpadRobot()
    assert testee.get_coordinates_for ('2') == Coordinates(1,2)
    assert testee.get_coordinates_for ('9') == Coordinates(2,0)
    
@pytest.mark.parametrize('start_key, target_key, expected_path', [
    ("A", "A", ""),
    ("1", "1", ""),
    ("7", "7", ""),
    ("A", "9", "^^^"),
    ("A", "6", '^^'),
    ("A", '7', '^^^<<'),
    ('7', '9', '>>'),
    ('7', 'A', '>>vvv'),
])
def test_numpad_robot_path_between_given_keys(start_key, target_key, expected_path):
    testee = NumpadRobot()
    testee.position = testee.get_coordinates_for(start_key)
    assert testee.go_to_key(target_key) == expected_path
    assert testee.current_position() == testee.get_coordinates_for(target_key)



@pytest.mark.parametrize('start_key, target_key, expected_path', [
    ("A", "A", ""),
    ("^", "^", ""),
    ("<", "A", ">>^"),
    ("A", "<", "v<<"),
])
def test_directionpad_robot_path_between_given_keys(start_key, target_key, expected_path):
    testee = DirectionpadRobot()
    testee.position = testee.get_coordinates_for(start_key)
    assert testee.go_to_key(target_key) == expected_path
    assert testee.current_position() == testee.get_coordinates_for(target_key)


def test_make_a_numpad_robot_press_0():
    testee = DirectionpadRobot()
    numpad_robot = NumpadRobot()
    testee.assign_robot_to_steer(numpad_robot)

    assert testee.make_numpad_press_key ('0') == 'v<<A' + '>>^A'
