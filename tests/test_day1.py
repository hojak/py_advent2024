from day1.vector_distance import single_distance, distance

import pytest

@pytest.mark.parametrize('a, b, expected', [
    (2, 2, 0),
    (10, 10, 0),
    (2, 10, 8),
    (10, 2, 8),
])
def test_single_distance(a, b, expected):
    assert single_distance(a,b) == expected


@pytest.mark.parametrize('listOfPairs, expectedDistance', [
    ([[1,1],[2,2]],0),
])
def test_distance(listOfPairs, expectedDistance):
    assert distance(listOfPairs) == expectedDistance
