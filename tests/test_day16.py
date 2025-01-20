from adv24Tools.Coordinates import Coordinates
from day16.ReindeerMaze import ReindeerMaze


def test_maze_with_start():
    testee = ReindeerMaze('###\n#S#\n###')
    assert testee.start_position() == Coordinates(1,1)