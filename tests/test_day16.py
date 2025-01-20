from adv24Tools.Coordinates import Coordinates
from day16.ReindeerMaze import ReindeerMaze
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