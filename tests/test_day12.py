import pytest

from adv24Tools.Coordinate import Coordinates
from day12.PlantArrangement import PlantArrangement


@pytest.mark.parametrize('input, coordinates, expected_result', [
    ('.X.\n.XX\n', Coordinates(1,1), 2),
])
def test_count_neighbors_with_same_plant(input, coordinates, expected_result):
    testee = PlantArrangement (input)
    assert testee.count_neighbors_with_same_plant(coordinates) == expected_result    