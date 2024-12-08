import pytest

from day7.tools import is_reachable, split_line, add_reachable_lines

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


def test_split_line():
    (number, list) = split_line ( "190: 10 19")
    assert number == 190
    assert list == [10, 19]


def test_add_reachable_lines():
    input = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''

    assert add_reachable_lines ( input ) == 3749
