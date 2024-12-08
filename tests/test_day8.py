import pytest

from day8.AntennaMap import AntennaMap
from adv24Tools.Coordinate import Coordinate

@pytest.mark.parametrize('input, frequency, expected_locations', [
    ('A', 'A', [Coordinate(0,0)]),
    ('AB', 'A', [Coordinate(0,0)]),    
    ('AB', 'B', [Coordinate(1,0)]),    
])
def test_finding_antennas(input, frequency, expected_locations) -> None:
    testee = AntennaMap(input)
    assert testee.get_antennas_for_frequency(frequency) == expected_locations
    



@pytest.mark.parametrize('input, expected_frequencies', [
    ('A', ['A']),
    ('ABAAB', ['A', 'B']),
])
def test_finding_frequencies(input, expected_frequencies) -> None:
    testee = AntennaMap(input)
    assert testee.get_found_frequencies() == expected_frequencies    
