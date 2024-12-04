from day1.vector_distance import single_distance, distance, similarityScore, countNumberOccurences

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
    ([[1,2],[1,2]],2),
    ([[2,1],[1,2]],0),
    ([[3,4],[4,3],[2,5],[1,3],[3,9],[3,3]],11)
])
def test_distance(listOfPairs, expectedDistance):
    assert distance(listOfPairs) == expectedDistance



@pytest.mark.parametrize('listOfPairs, expectedSimilarityScore', [
    ([[1,1],[2,2]],3),
    ([[1,3],[2,3]],0),
    ([[3,4],[4,3],[2,5],[1,3],[3,9],[3,3]],31)
])
def test_similarityScore(listOfPairs, expectedSimilarityScore):
    assert similarityScore(listOfPairs) == expectedSimilarityScore


def test_countNumberOccurences():
    countHash = countNumberOccurences([1,2,2,1,5])
    assert countHash[7] == 0
    assert countHash[1] == 2
    assert countHash[5] == 1
    assert countHash[1] == 2
