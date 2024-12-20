from adv24Tools.Coordinates import Coordinates

from day18.MemoryGrid import MemoryGrid, parse_coordinates


def test_create_grid():
    height = 10
    width = 12
    testee = MemoryGrid(width, height)
    assert height == testee.get_height()
    assert width == testee.get_width()


def test_mark_corruption():
    height = 10
    width = 12
    testee = MemoryGrid(width, height)

    testee.mark_corruption(Coordinates ( 5,6))

    assert not testee.is_accessible(Coordinates ( 5,6))


def test_steps_to_exit():
    corruptions = '''5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
'''

    testee = MemoryGrid(7,7)

    for coordinates in parse_coordinates ( corruptions ):
        testee.mark_corruption(coordinates)

    assert 22 == testee.steps_to_exit( Coordinates(0,0), Coordinates(6,6) )
