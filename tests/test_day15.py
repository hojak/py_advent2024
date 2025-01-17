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
    ("####\n#@.#\n####", ">", "####\n#.@#\n####"),
])
def test_simple_movement(initial_map, direction, expected_resulting_map):
    testee = Warehouse(initial_map)
    testee.move(direction)
    assert testee.__str__() == expected_resulting_map