from day25.Keyhole import Keyhole


def test_create_simple_keyhole ():
    testee = Keyhole ( "#####\n.....\n.....\n.....\n.....\n.....\n.....")
    expected_heights = [0,0,0,0,0]
    for index in range(len(expected_heights)):
        assert testee.get_height(index) == expected_heights[index]
