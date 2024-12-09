import pytest

from day9.tools import expand

@pytest.mark.parametrize('input, expected_expandation', [
    ('12345', [0,'.','.',1,1,1,'.','.','.','.',2,2,2,2,2]),
    ('2333133121414131402', [0,0,'.','.','.',1,1,1,'.','.','.',2,'.','.','.',3,3,3,'.',4,4,'.',5,5,5,5,'.',6,6,6,6,'.',7,7,7,'.',8,8,8,8,9,9] )
])
def test_expand(input, expected_expandation) -> None:
    assert expand ( input ) == expected_expandation
