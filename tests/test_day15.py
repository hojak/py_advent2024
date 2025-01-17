from adv24Tools.Coordinates import Coordinates
from day15.Warehouse import Warehouse
import pytest

def test_initial_map_with_robot():
    testee = Warehouse (
        "####\n"+
        "#..#\n"+
        "#@.#\n"+
        "####"
    )
    
    assert testee.get_robot_position() == Coordinates (1,2)


@pytest.mark.parametrize('initial_map, direction, expected_resulting_map', [
    ("####\n#@.#\n####", ">", "####\n#.@#\n####"), # walk right
    ("####\n#.@#\n####", "<", "####\n#@.#\n####"), # walk left
    ("####\n#.@#\n#..#\n####", "v", "####\n#..#\n#.@#\n####"), # walk down
    ("####\n#..#\n#.@#\n####", "^", "####\n#.@#\n#..#\n####"), # walk up
    ("####\n#@.#\n####", "<", "####\n#@.#\n####"), # don't run into a wall
    ("#####\n#@O.#\n#####", ">", "#####\n#.@O#\n#####"), # push a box to the right
    ("#####\n#.O@#\n#####", "<", "#####\n#O@.#\n#####"), # push a box to the left
    ("####\n#@O#\n####", ">", "####\n#@O#\n####"), # don't push a box into a wall
    ("########\n#@OOOO.#\n########", ">", "########\n#.@OOOO#\n########"), # push multiple boxes to the right
    ("#######\n#@OOOO#\n#######", ">", "#######\n#@OOOO#\n#######"), # don't push multiple boxes into a wall
])
def test_simple_movement(initial_map, direction, expected_resulting_map):
    testee = Warehouse(initial_map)
    testee.move(direction)
    assert testee.__str__() == expected_resulting_map


def test_follow_a_plan():
    testee = Warehouse(
'''########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########'''
    )
    testee.follow_plan('<^^>>>vv<v>>v<<')

    assert testee.__str__() == '''########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########'''
    