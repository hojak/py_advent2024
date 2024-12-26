from day22.tools import *

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


@pytest.mark.parametrize('base, steps, expected', [
    (10,0,10),
    (123, 1, 15887950),
    (123, 2, 16495136),
    (1, 2000, 8685429),
    (10, 2000, 4700978),
    (100, 2000, 15273692),
    (2024, 2000, 8667524),
])
def test_apply_n_sectret_steps (base, steps, expected):
    assert apply_n_secret_steps(base, steps) == expected

def test_sum_for_buyers():
    assert sum_for_buyers([1,10,100,2024]) == 37327623


@pytest.mark.parametrize('value, expected_price', [
    (10,0),
    (103,3),
    (124123423,3),
])
def test_get_price(value, expected_price):
    assert get_price ( value) == expected_price


def test_sequence_str():
    assert str(Sequence ([1,2,3,4])) == "1/2/3/4"

def test_next_sequence():
    assert Sequence([1,2,3,4]).next(5) == Sequence ([2,3,4,5])