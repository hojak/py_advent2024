import pytest

from adv24Tools.Coordinates import Coordinates
from day12.PlantArrangement import PlantArrangement

@pytest.mark.parametrize('input, start_point, expected_result', [
    ('X', Coordinates(1,1), 1),
])
def test_area_size(input, start_point, expected_result):
    testee = PlantArrangement (input)
    assert testee.get_area_size(start_point) == expected_result


@pytest.mark.parametrize('input, coordinates, expected_result', [
    ('.X.\n.XX\n', Coordinates(1,1), 2),
])
def test_count_neighbors_with_same_plant(input, coordinates, expected_result):
    testee = PlantArrangement (input)
    assert testee.count_neighbors_with_same_plant(coordinates) == expected_result    