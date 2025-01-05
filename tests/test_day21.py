from day21.NumpadRobot import NumpadRobot
from adv24Tools.Coordinates import Coordinates


def test_numpad_robot_create ():
    testee = NumpadRobot()
    assert testee.current_position() == Coordinates (2,3)
    assert testee.current_key() == 'A'


def test_robot_get_coordinates_of_key():
    testee = NumpadRobot()
    assert testee.get_coordinates_for ('2') == Coordinates(1,2)
    assert testee.get_coordinates_for ('9') == Coordinates(2,0)
    

@pytest.mark.parametrize('key', [
    ("A"),
    ("1"),
    ("7"),
])
def test_numpad_robot_path_to_current_key(key):
    testee = NumpadRobot()
    testee.position = testee.get_coordinates_for(key)
    assert testee.go_to_key (key) == ""


def test_numpad_robot_path_from_A_to_A():
    testee = NumpadRobot()
    assert testee.go_to_key ('A') == ""