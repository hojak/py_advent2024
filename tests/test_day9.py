import pytest

from day9.tools import expand, compact

@pytest.mark.parametrize('input, expected_expandation', [
    ('12345', [0,'.','.',1,1,1,'.','.','.','.',2,2,2,2,2]),
    ('2333133121414131402', [0,0,'.','.','.',1,1,1,'.','.','.',2,'.','.','.',3,3,3,'.',4,4,'.',5,5,5,5,'.',6,6,6,6,'.',7,7,7,'.',8,8,8,8,9,9] )
])
def test_expand(input, expected_expandation) -> None:
    assert expand ( input ) == expected_expandation


@pytest.mark.parametrize('input, expected_result', [
    ([0,'.','.',1,1,1,'.','.','.','.',2,2,2,2,2], [0,2,2,1,1,1,2,2,2,'.','.','.','.','.','.']),
    ([0,0,'.','.','.',1,1,1,'.','.','.',2,'.','.','.',3,3,3,'.',4,4,'.',5,5,5,5,'.',6,6,6,6,'.',7,7,7,'.',8,8,8,8,9,9],
       [0,0,9,9,8,1,1,1,8,8,8,2,7,7,7,3,3,3,6,4,4,6,5,5,5,5,6,6,'.','.','.','.','.','.','.','.','.','.','.','.','.','.']  )
])
def test_compact(input, expected_result):
    assert compact ( input ) == expected_result
