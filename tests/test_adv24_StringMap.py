import pytest

from adv24Tools.StringMap import StringMap
from adv24Tools.Coordinates import Coordinates


@pytest.mark.parametrize('init, location, expected', [
    ('aaa\nbbb\nccc', Coordinates(1,1), 'aaa\nbXb\nccc'),
    ('aaa\nbbb\nccc', Coordinates(0,0), 'Xaa\nbbb\nccc'),
    ('aaa\nbbb\nccc', Coordinates(2,2), 'aaa\nbbb\nccX'),
])
def test_set_char_at(init, location, expected):
    testee = StringMap(init)
    testee.set_char_at ( location, "X")
    assert str(testee) == expected