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
])
def test_score_path(path, expected_score):
    testee = ReindeerPath(path)
    assert testee.score() == expected_score