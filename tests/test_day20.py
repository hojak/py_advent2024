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
    assert  expected_start == testee.start()
    assert expected_end == testee.end()