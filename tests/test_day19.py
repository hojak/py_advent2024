from day19.tools import *
import pytest

def test_parse_available_towels():
    assert ['a', 'bb', 'cde'] == parse_available_towels('a, bb, cde')


@pytest.mark.parametrize('pattern, expected', [
    ('a', True),
    ('aaaa', True),
    ('aaba', True),
    ('abcc', True),
    ('aacc', True),
    ('aXaba', False),
    ('aX', False),
])
def test_is_pattern_possible(pattern, expected):
    available = ['a', 'ab', 'cc']
    assert expected == is_pattern_possible(pattern, available)


def test_count_possible_patterns ():
    towels = parse_available_towels('r, wr, b, g, bwu, rb, gb, br')

    desired_patterns = re.split ( '\n', '''brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb''')

    assert 6 == count_possible_patterns(desired_patterns, towels)


@pytest.mark.parametrize('pattern, expected', [
    ('a', 1),
    ('aaaa', 1),
    ('aaba', 1),
    ('abcc', 1),
    ('aacc', 1),
    ('aXaba', 0),
    ('aX', 0),
    ('dd', 2),
    ('ddd', 3),
    ('dddd', 1+2+2),
])
def test_count_possible_solutions(pattern, expected):
    available = ['a', 'ab', 'cc', 'd', 'dd']
    assert expected == count_possible_solutions(pattern, available)


def test_count_all_solutions ():
    towels = parse_available_towels('r, wr, b, g, bwu, rb, gb, br')

    desired_patterns = re.split ( '\n', '''brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb''')

    assert 16 == count_all_solutions(desired_patterns, towels)    