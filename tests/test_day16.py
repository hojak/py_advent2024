from adv24Tools.Coordinates import Coordinates
from day16.ReindeerMaze import ReindeerMaze, ReindeerPath
import pytest


@pytest.mark.parametrize('map_description, expected_start_position', [
    ('####\n#SE#\n####', Coordinates(1,1)), 
    ('####\n#E.#\n#.S#\n####', Coordinates(2,2)), 
])
def test_maze_with_start(map_description, expected_start_position):
    testee = ReindeerMaze(map_description)
    assert testee.start_position == expected_start_position

@pytest.mark.parametrize('map_description, expected_end_position', [
    ('####\n#ES#\n####', Coordinates(1,1)), 
    ('####\n#S.#\n#.E#\n####', Coordinates(2,2)), 
])
def test_maze_with_end(map_description, expected_end_position):
    testee = ReindeerMaze(map_description)
    assert testee.end_position == expected_end_position


def test_reindeer_start_position_and_heading():
    testee = ReindeerMaze('####\n#S.#\n#.E#\n####')
    assert testee.reindeer_position == Coordinates(1,1)
    assert testee.reindeer_heading == ReindeerMaze.Headings.east


@pytest.mark.parametrize('path, expected_score', [
    ([ReindeerPath.Step.forward], 1), 
    ([ReindeerPath.Step.forward, ReindeerPath.Step.forward, ReindeerPath.Step.forward], 3), 
    ([ReindeerPath.Step.forward, ReindeerPath.Step.turn_right, ReindeerPath.Step.forward, ReindeerPath.Step.turn_left, ReindeerPath.Step.forward], 2003), 
])
def test_score_path(path, expected_score):
    testee = ReindeerPath(Coordinates(1,1), Coordinates(1,1), path)
    assert testee.score() == expected_score


@pytest.mark.parametrize('maze, expected_score', [
    ('####\n#SE#\n####', 1), # one simple step top the east
    ('######\n#S..E#\n######', 3), # score for three steps to the east
    ('###\n#S#\n#.#\n#E#\n###', 1002), # rotate right at start
    ('###\n#E#\n#.#\n#S#\n###', 1002), # rotate left at start
    ('######\n#E..S#\n######', 2003), # turn around at the start
    ('####\n#S.#\n##E#\n####\n',1002), # turn once on the way
])
def test_find_the_way(maze, expected_score):
    testee = ReindeerMaze(maze)
    assert testee.lowest_score_for_path_to_finish() == expected_score

@pytest.mark.parametrize('maze, path_so_far, expected_possible_steps', [
    ('#####\n#...#\n#.S.#\n#..E#\n#####', ReindeerPath(Coordinates(2,2), ReindeerMaze.Headings.east), [ReindeerPath.Step.forward, ReindeerPath.Step.turn_left, ReindeerPath.Step.turn_right]),     
])
def test_possible_nenxt_steps(maze, path_so_far, expected_possible_steps):
    testee = ReindeerMaze(maze)
    assert set(testee.possible_next_steps(path_so_far)) == set(expected_possible_steps)