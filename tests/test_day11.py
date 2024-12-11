import pytest

from day11.tools import blink

@pytest.mark.parametrize('input, expected_list', [
    ([0], [1] )
])
def test_blink(input, expected_list):
    assert blink (input) == expected_list