from day19.tools import parse_available_towels


def test_parse_available_towels():
    assert ['a', 'bb', 'cde'] == parse_available_towels('a, bb, cde')