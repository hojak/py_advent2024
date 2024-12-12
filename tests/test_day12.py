import pytest

from adv24Tools.Coordinates import Coordinates
from day12.PlantArrangement import PlantArrangement

@pytest.mark.parametrize('input, start_point, expected_result', [
    ('X', Coordinates(0,0), 1),
 #   ('XX\nXX', Coordinates(1,1), 4),
    ('XXX\nXAX\nXXX', Coordinates(1,1), 1),
    ('XXX\nXAX\nXXX', Coordinates(0,0), 8),
])
def test_area_of_region(input, start_point, expected_result):
    testee = PlantArrangement (input)
    result = testee.get_data_of_region(start_point)
    assert result['area'] == expected_result


@pytest.mark.parametrize('input, coordinates, expected_result', [
    ('.X.\n.XX\n', Coordinates(1,1), 2),
])
def test_count_neighbors_with_same_plant(input, coordinates, expected_result):
    testee = PlantArrangement (input)
    assert testee.count_neighbors_with_same_plant(coordinates) == expected_result    