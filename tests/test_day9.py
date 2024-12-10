import pytest

from day9.tools import expand, compact, checksum, expand_to_blocks, move_blocks, checksum_for_blocks

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


@pytest.mark.parametrize('input, expected_checksum', [
    ([0,2,2,1,1,1,2,2,2,'.','.','.','.','.','.'], 0 + 2*1 + 2*2 + 3 + 4 + 5 + 2*6 + 2*7 + 2*8),
    ([0,0,9,9,8,1,1,1,8,8,8,2,7,7,7,3,3,3,6,4,4,6,5,5,5,5,6,6,'.','.','.','.','.','.','.','.','.','.','.','.','.','.'], 1928  )
])
def test_compact(input, expected_checksum):
    assert checksum ( input ) == expected_checksum


@pytest.mark.parametrize('input, expected_expandation', [
    ('12345', [[1,0],[2,'.'],[3,1],[4,'.'],[5,2]]),
    ('2333133121414131402', [[2,0],[3,'.'],[3,1],[3,'.'],[1,2],[3,'.'],[3,3],[1,'.'],[2,4],[1,'.'],[4,5],[1,'.'],[4,6],[1,'.'],[3,7],[1,'.'],[4,8],[2,9]] )
])
def test_expand_to_blocks(input, expected_expandation) -> None:
    assert expand_to_blocks ( input ) == expected_expandation



@pytest.mark.parametrize('input, expected_layout', [
    ([[1,0],[2,'.'],[3,1],[4,'.'],[5,2]],  [[1,0],[2,'.'],[3,1],[4,'.'],[5,2]]),
    ([[2,0],[3,'.'],[3,1],[3,'.'],[1,2],[3,'.'],[3,3],[1,'.'],[2,4],[1,'.'],[4,5],[1,'.'],[4,6],[1,'.'],[3,7],[1,'.'],[4,8],[2,9]],
        [[2,0],[2,9],[1,2],[3,1],[3,7],[1,'.'],[2,4],[1,'.'],[3,3],[4,'.'],[4,5],[1,'.'],[4,6],[5,'.'],[4,8],[2,'.']],
      )
])
def test_moving_blocks(input, expected_layout) -> None:
    assert move_blocks ( input ) == expected_layout


def test_checksum_for_blocks (): 
    assert checksum_for_blocks (  [[2,0],[2,9],[1,2],[3,1],[3,7],[1,'.'],[2,4],[1,'.'],[3,3],[4,'.'],[4,5],[1,'.'],[4,6],[5,'.'],[4,8],[2,'.']] ) == 2858