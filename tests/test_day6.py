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



@pytest.mark.parametrize('map',[
    '<.#.\n....\n.#..',
    '..#.\n..v.\n.#..',
    '..#.\n....\n.#.>',
])
def test_str(map) -> None:
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



@pytest.mark.parametrize('map, expected_trail', [
    ('>...\n....', 'X   \n    '),
    ('....\n..^.', '    \n  X '),
    ('....\n...<', '    \n   X'),
])
def test_start_trail(map, expected_trail) -> None:
    testee = LabMap(map)
    assert testee.get_trail() == expected_trail


@pytest.mark.parametrize('map, expected_trail', [
    ('>...\n....', 'XXXX\n    '),
    ('>.#.\n....', 'XX  \n X  '),
])
def test_run_patrol(map, expected_trail):
    testee = LabMap (map)
    testee.run_patrol()
    assert testee.get_trail() == expected_trail


@pytest.mark.parametrize('map, expected_length', [
    ('>...\n....', 4),
    ('>.#.\n....', 3),
    ('''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...''', 41)
])
def test_run_patrol(map, expected_length):
    testee = LabMap (map)
    testee.run_patrol()
    assert testee.get_trail_length() == expected_length





@pytest.mark.parametrize('map, expected_result', [
    ('>...\n....', False),
])
def test_is_loop(map, expected_result):
    testee = LabMap ( map)
    assert testee.is_loop () == expected_result