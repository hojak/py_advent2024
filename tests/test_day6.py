import pytest

from day6.LabMap import LabMap, GuardStatus

@pytest.mark.parametrize('init_str, expected_width', [
    ('''....
.^..
....''', 4),
])
def test_width(init_str, expected_width) -> None:
    testee = LabMap(init_str)
    assert testee.get_width() == expected_width


def test_str() -> None:
    map = '''..#.
..v.
.#..'''
    testee = LabMap(map)
    assert testee.__str__() == map 



@pytest.mark.parametrize('init_str, expected_status', [
    ('''....
.^..
....''', GuardStatus(1,1,'^')),
    ('''....
....
..v.
''', GuardStatus(2,2,'v')),
])
def test_start_guide_status(init_str, expected_status) -> None:
    testee = LabMap(init_str)
    assert testee.get_guard_status() == expected_status


@pytest.mark.parametrize('init_str, expected_result', [
    ('''>.''', '''.>'''),
    ('.....\n..<..', '.....\n.<...'),
    ('..\n^.', '^.\n..'),
    ('.v\n..', '..\n.v'),

    ('>#\n..', 'v#\n..'),
    ('#<\n..', '#^\n..'),
    ('.#\n.^', '.#\n.>'),
    ('v.\n#.', '<.\n#.'),
])
def test_walk_guard(init_str, expected_result) -> None:
    testee = LabMap(init_str)
    testee.walk_guard()
    assert testee.__str__() == expected_result

def test_start_trail() -> None:
    testee = LabMap('...\n.<.\n...')
    assert testee.get_trail() == '   \n X \n   '

