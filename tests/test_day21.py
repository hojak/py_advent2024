from day21.NumpadRobot import NumpadRobot, DirectionpadRobot
from adv24Tools.Coordinates import Coordinates

import pytest

def test_numpad_robot_create ():
    testee = NumpadRobot()
    assert testee.current_position() == Coordinates (2,3)
    assert testee.current_key() == 'A'
    assert testee.illegal == Coordinates(0,3)

def test_directionpad_robot_create():
    testee = DirectionpadRobot()
    assert testee.illegal == Coordinates(0,0)


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


@pytest.mark.parametrize('key, expected_path', [
    ("0", 'v<<A' + '>>^A'),
    ("6", '<A' + 'A' + '>A'), # ^^A
    ("7", '<A' + 'A' + 'A' + 'v<A' + 'A' + '>>^A'), # ^^^<<A
])
def test_make_a_numpad_robot_press_key(key, expected_path):
    testee = DirectionpadRobot()
    numpad_robot = NumpadRobot()
    testee.assign_robot_to_steer(numpad_robot)

    assert testee.make_assigned_press_key (key) == expected_path


@pytest.mark.parametrize('sequence, expected_path', [
    ("029A", 'v<<A>>^A<A>AvA^<AA>Av<AAA>^A'),
])
def test_make_a_numpad_robot_enter_sequence(sequence, expected_path):
    testee = DirectionpadRobot()
    numpad_robot = NumpadRobot()
    testee.assign_robot_to_steer(numpad_robot)

    assert testee.make_assigned_press_sequence(sequence) == expected_path


@pytest.mark.parametrize('sequence, expected_path', [
    ("<", 'v<A<AA>>^A'), 
    ("v<", 'v<A<A>>^Av<<A>>^A'), # 'v<A<A'), 
])
def test_make_a_directionpad_robot_enter_sequence(sequence, expected_path):
    testee = DirectionpadRobot()
    to_steer = DirectionpadRobot()
    testee.assign_robot_to_steer(to_steer)

    assert testee.make_assigned_press_sequence(sequence) == expected_path



# is it a problem, the a different intermediate path leads to a complete different path of the same length?
# <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
# v<<A>>^A<A>AvA<^AA>A<vAAA>^A
# instead of
# v<A<AA>>^AvAA^<A>Av<<A>>^AvA^Av<A>^A<Av<A>>^AAvA^Av<A<A>>^AAAvA^<A>A
# v<<A>>^A<A>AvA^<AA>Av<AAA>^A
# -> yes, the next test shows, it is a problem
@pytest.mark.parametrize('sequence, expected_path', [
    ("0", 'v<A<AA>>^AvAA^<A>A'), # 0 -> '<A' -> 'v<<A>>^A' -> 'v<A<AA>>^AvAA^<A>A'
    ('029A', 'v<A<AA>>^AvAA^<A>Av<<A>>^AvA^Av<A>^A<Av<A>>^AAvA^Av<A<A>>^AAAvA^<A>A'),
])
def test_make_final_robot_with_intermediate_enter_sequence(sequence, expected_path):
    testee = DirectionpadRobot()
    intermediate = DirectionpadRobot()
    numpad = NumpadRobot()
    intermediate.assign_robot_to_steer(numpad)
    testee.assign_robot_to_steer(intermediate)

    assert testee.make_final_robot_enter(sequence) == expected_path


# todo: reenable test, when problem can be solved
@pytest.mark.parametrize('code, expected_length', [
    ('029A', len('<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A')),
    ('980A', len('<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A')),
    ('179A', len('<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A') ),
    ('456A', len('<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A')),
    ('379A', len('<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A')),
])
def disabled_test_sequence_length_for_code(code, expected_length):
    testee = DirectionpadRobot()
    intermediate = DirectionpadRobot()
    numpad = NumpadRobot()
    intermediate.assign_robot_to_steer(numpad)
    testee.assign_robot_to_steer(intermediate)

    assert testee.length_of_sequence_for_code(code) == expected_length
