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

@pytest.mark.parametrize('init_str, expected_height', [
    ('''....
.^..
....''', 3),
    ('''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...''', 10)
])
def test_height(init_str, expected_height) -> None:
    testee = LabMap(init_str)
    assert testee.get_height() == expected_height


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
    ('.#..\n.>.#\n#...\n..#.', True),
])
def test_is_loop(map, expected_result):
    testee = LabMap ( map)
    assert testee.ends_in_loop () == expected_result


@pytest.mark.parametrize('map, expected_result', [
    ('>...\n....', False),
    ('.#..\n..>.\n#...\n..#.', True),
])
def test_is_next_posistion_a_possible_loop_obstacle(map, expected_result):
    testee = LabMap ( map)
    assert testee.is_next_posistion_a_possible_loop_obstacle () == expected_result



@pytest.mark.parametrize('map, expected_obstacle_count', [
    ('>...\n....', 0),
    ('.#..\n.>..\n#...\n..#.', 1),
    ('.#..\n..>.\n#...\n..#.', 1),
    ('''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...''', 6)
])
def test_run_patrol_counts_possible_obstacles(map, expected_obstacle_count):
    testee = LabMap (map)
    testee.run_patrol()
    assert testee.get_number_of_possible_obstacles() == expected_obstacle_count


@pytest.mark.parametrize('map, expected_obstacle_count', [
    ('>...\n....', []),
    ('.#..\n.>..\n#...\n..#.', [7]),
    ('.#..\n..>.\n#...\n..#.', [7]),

])
def test_run_patrol_get_possible_obstacles(map, expected_obstacle_count):
    testee = LabMap (map)
    testee.run_patrol()
    assert testee.get_possible_obstacle_locations() == expected_obstacle_count
