from day1.vector_distance import single_distance, distance, similarity_score, count_number_of_occurences

import pytest

@pytest.mark.parametrize('a, b, expected', [
    (2, 2, 0),
    (10, 10, 0),
    (2, 10, 8),
    (10, 2, 8),
])
def test_single_distance(a, b, expected):
    assert single_distance(a,b) == expected


@pytest.mark.parametrize('list_of_pairs, expected_distance', [
    ([[1,1],[2,2]],0),
    ([[1,2],[1,2]],2),
    ([[2,1],[1,2]],0),
    ([[3,4],[4,3],[2,5],[1,3],[3,9],[3,3]],11)
])
def test_distance(list_of_pairs, expected_distance):
    assert distance(list_of_pairs) == expected_distance



@pytest.mark.parametrize('list_of_pairs, expected_similarity_score', [
    ([[1,1],[2,2]],3),
    ([[1,3],[2,3]],0),
    ([[3,4],[4,3],[2,5],[1,3],[3,9],[3,3]],31)
])
def test_similarity_score(list_of_pairs, expected_similarity_score):
    assert similarity_score(list_of_pairs) == expected_similarity_score


def test_count_number_of_occurences():
    count_hash = count_number_of_occurences([1,2,2,1,5])
    assert count_hash[7] == 0
    assert count_hash[1] == 2
    assert count_hash[5] == 1
    assert count_hash[1] == 2
