import pytest

from day8.AntennaMap import AntennaMap
from adv24Tools.Coordinate import Coordinates

@pytest.mark.parametrize('input, frequency, expected_locations', [
    ('A', 'A', [Coordinates(0,0)]),
    ('AB', 'A', [Coordinates(0,0)]),    
    ('AB', 'B', [Coordinates(1,0)]),    
])
def test_finding_antennas(input, frequency, expected_locations) -> None:
    testee = AntennaMap(input)
    assert testee.get_antennas_for_frequency(frequency) == expected_locations
    

@pytest.mark.parametrize('input, expected_frequencies', [
    ('A', ['A']),
    ('A...', ['A']),
    ('ABAAB', ['A', 'B']),
])
def test_finding_frequencies(input, expected_frequencies) -> None:
    testee = AntennaMap(input)
    assert testee.get_found_frequencies() == expected_frequencies    

@pytest.mark.parametrize('map, coor1, coor2, expected_antinodes', [
    ('...\n...\n...\n...', Coordinates(1,1), Coordinates(1,2), [Coordinates(1,0), Coordinates(1,3)]),
])
def test_finding_antinodes(map, coor1, coor2, expected_antinodes) -> None:
    testee = AntennaMap(map)
    possible_antinotes = testee.find_antinodes(coor1, coor2)
    assert possible_antinotes == expected_antinodes


def test_count_all_antinodes ():
    map = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''

    testee = AntennaMap(map)

    assert testee.get_number_of_antinodes() == 14