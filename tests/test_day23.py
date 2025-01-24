from day23.Network import Network

def test_init_network_has_computers():
    testee = Network('aa-ab\ncc-dd')
    assert set(testee.get_computers()) == set (['aa', 'ab', 'cc', 'dd'])