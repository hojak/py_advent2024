import pytest

from day11.tools import blink

@pytest.mark.parametrize('input, expected_list', [
    ([0], [1]),
    ([11, 0], [1,1,1]),
    ([1000, 0], [10, 0, 1]),
    ([1000, 0, 2], [10, 0, 1, 4048]),
])
def test_blink(input, expected_list):
    assert blink (input) == expected_list

@pytest.mark.parametrize('input, blinks, expected_output', [
    ([125, 17], 6, [2097446912, 14168, 4048, 2, 0, 2, 4, 40, 48, 2024, 40, 48, 80, 96, 2, 8, 6, 7, 6, 0, 3, 2]),
])
def test_multiple_blinks(input, blinks, expected_output):
    result = input
    for i in range(blinks):
        result = blink(result)
    assert result == expected_output