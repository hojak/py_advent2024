from day25.Keyhole import Keyhole
from day25.Key import Key
import pytest

@pytest.mark.parametrize('init_string, expected_heights', [
    ("#####\n.....\n.....\n.....\n.....\n.....\n.....", [0,0,0,0,0]),
    ("#####\n#....\n.....\n.....\n.....\n.....\n.....", [1,0,0,0,0]),
    ("#####\n#...#\n....#\n....#\n....#\n....#\n.....", [1,0,0,0,5]),
])
def test_create_keyholes (init_string, expected_heights):
    testee = Keyhole ( init_string)
    for column in range(len(expected_heights)):
        assert testee.get_height(column) == expected_heights[column]


@pytest.mark.parametrize('init_string, expected_heights', [
    (".....\n.....\n.....\n.....\n.....\n.....\n#####", [0,0,0,0,0]),
    (".....\n....#\n....#\n....#\n....#\n#...#\n#####", [1,0,0,0,5]),
])
def test_create_keys (init_string, expected_heights):
    testee = Key ( init_string)
    for column in range(len(expected_heights)):
        assert testee.get_height(column) == expected_heights[column]
