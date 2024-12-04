import pytest

from day3.word_riddle import WordRiddle

@pytest.mark.parametrize('init_str, expected_width', [
    ('X', 1),
    ('XM\nAS', 2),
    ('XMA\nAXM', 3),
])
def test_get_width(init_str,expected_width) -> None:
    testee = WordRiddle(init_str)
    assert testee.get_width() == expected_width

@pytest.mark.parametrize('init_str, expected_height', [
    ('X', 1),
    ('XM\nAS', 2),
    ('XMA\nAXM', 2),
])
def test_get_width(init_str,expected_height) -> None:
    testee = WordRiddle(init_str)
    assert testee.get_height() == expected_height


