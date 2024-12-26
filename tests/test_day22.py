from day22.tools import mix_in, prune, next_secret_value

import pytest


@pytest.mark.parametrize('a, b, expected', [
    (3,5,6),
    (2,10,8),
    (15,42,37),
])
def test_mix_in(a, b, expected):   
    assert mix_in(a, b) == expected

@pytest.mark.parametrize('value, expected', [
    (100000000, 16113920)
])
def test_prune(value, expected):
    assert prune ( value ) == expected

@pytest.mark.parametrize('value, expected', [
    (123, 15887950),
    (15887950, 16495136),
    (16495136, 527345),
    (527345, 704524),
    (704524, 1553684),
])
def test_next_secret_value(value, expected):
    assert next_secret_value(value) == expected
