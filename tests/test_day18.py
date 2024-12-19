from adv24Tools.Coordinates import Coordinates

from day18.MemoryGrid import MemoryGrid


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