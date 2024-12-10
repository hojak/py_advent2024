import pytest

from adv24Tools.Coordinate import Coordinates
from day10.TopographicMap import TopographicMap

@pytest.mark.parametrize('map, location, expected_score', [
    ('0123\n1234\n8765\n9876', Coordinates(0,0), 1  )
])
def test_score_of_location(map, location, expected_score) -> None:
    testee = TopographicMap(map)
    assert testee.score_of_location(location) == 1

@pytest.mark.parametrize('map, expected_score', [
    ('0123\n1234\n8765\n9876', 1  ),
    ('''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732''', 36)
])
def test_sum_of_scores(map, expected_score) -> None:
    testee = TopographicMap(map)
    assert testee.sum_of_scores() == expected_score


@pytest.mark.parametrize('map, expected_score', [
    ('0123\n1234\n8765\n9876', 16  ),
    ('''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732''', 81)
])
def test_sum_of_scores(map, expected_score) -> None:
    testee = TopographicMap(map)
    assert testee.number_of_different_trails() == expected_score
