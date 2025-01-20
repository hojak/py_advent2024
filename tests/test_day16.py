from adv24Tools.Coordinates import Coordinates
from day16.ReindeerMaze import ReindeerMaze
import pytest


@pytest.mark.parametrize('map_description, expected_start_position', [
    ('###\n#S#\n###', Coordinates(1,1)), 
    ('####\n#..#\n#.S#\n####', Coordinates(2,2)), 
])
def test_maze_with_start(map_description, expected_start_position):
    testee = ReindeerMaze(map_description)
    assert testee.start_position == expected_start_position