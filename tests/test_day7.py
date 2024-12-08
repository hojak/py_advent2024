import pytest

from day7.tools import is_reachable

@pytest.mark.parametrize('target, numbers, expected_result', [
    (10, [10], True),
    (10, [11], False),
    (10, [2,5], True),
    (9, [2,5], False),
    (190, [10,19],True),
    (3267, [81,40,27],True),
    (83, [17,5],False),
    (156, [15,6],False),
    (7290, [6,8,6,15],False),
    (161011, [16,10,13],False),
    (192, [17,8,14],False),
    (21037, [9,7,18,13],False),
    (292, [11,6,16,20],True),
])
def test_is_reachable(target, numbers, expected_result) -> None:
    assert is_reachable(target, numbers) == expected_result