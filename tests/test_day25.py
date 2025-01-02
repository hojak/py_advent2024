from day25.Keyhole import Keyhole

def test_create_keyhole ():
    testee = Keyhole ( "#####\n.....\n.....\n.....\n.....\n.....\n.....")
    assert isinstance(testee, Keyhole)