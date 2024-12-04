import pytest

from day4.word_riddle import WordRiddle

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


@pytest.mark.parametrize('init_str, x, y, length, direction, expected_chars', [
    ('X',0,0,1,'r', 'X'),
    ('XMAS',0,0,2,'r', 'XM'),
    ('XMAS',1,0,2,'r', 'MA'),
    ('XMAS',2,0,2,'r', 'AS'),
    ('X',0,0,2,'r', ''),
    ('A\nA',0,1,3,'u', ''),
    ('XX',1,0,3,'l', ''),
    ('X\nX\nI',0,1,3,'d', ''),    
    ('X\nM\nA',0,1,2,'d', 'MA'),    
    ('...S\n..A.\n.M..\nX...',0,3,4,'ru', 'XMAS'),    
])
def test_get_chars_in_direction(init_str: str,x:int,y:int,direction:str,length:int,expected_chars:str) -> None:
    testee = WordRiddle(init_str)
    assert testee.get_chars_in_direction(x,y,direction,length) == expected_chars


def test_find_XMAS() -> None:
    testee = WordRiddle(
'''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX''')
    assert testee.number_of_occurences('XMAS') == 18