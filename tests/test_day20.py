from day20.RaceMap import RaceMap
from adv24Tools.Coordinates import Coordinates

def test_start_and_end():
    testee = RaceMap('''###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############''')
    
    expected_start = Coordinates(1,3)
    expected_end = Coordinates(5,7)
    assert expected_start == testee.start()
    assert expected_end == testee.end()
    assert 84 == testee.length_of_path(testee.start(), testee.end())


def test_length_of_cheat():
    testee = RaceMap('''###############
#OOO#...#.....#
#O#O#.#.#.###.#
#O#OOO#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############''')
    assert 72 == testee.length_of_cheat( Coordinates(6,3), Coordinates(7,3))
    assert -1 == testee.length_of_cheat( Coordinates(10,2), Coordinates(11,2))
    