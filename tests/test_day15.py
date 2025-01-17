from adv24Tools.Coordinates import Coordinates
from day15.Warehouse import Warehouse

def test_initial_map_with_robot():
    testee = Warehouse (
        "####\n"+
        "#..#\n"+
        "#@.#\n"+
        "####"
    )
    
    assert testee.get_robot_position() == Coordinates (1,2)

def test_simple_movement():
    testee = Warehouse(
        "####\n"+
        "#@.#\n"+
        "####"
    )
    testee.move(">")
    assert testee.__str__() == "####\n" + "#.@#\n" + "####"