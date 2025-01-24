from day23.Network import Network

def test_init_network_has_computers():
    testee = Network('aa-ab\ncc-dd')
    assert set(testee.get_computers()) == set (['aa', 'ab', 'cc', 'dd'])

def test_computers_are_connected():
    testee = Network('aa-ab\ncc-dd')
    assert testee.has_connection('aa', 'ab')
    assert testee.has_connection('ab', 'aa')

def test_computers_are_not_connected():
    testee = Network('aa-ab\ncc-dd')
    assert not testee.has_connection('aa', 'cc')
    assert not testee.has_connection('ab', 'dd')

def test_find_network_of_three():
    testee = Network('aa-bb\naa-dd\naa-cc\ncc-bb')
    assert testee.has_connection('aa', 'cc')
    assert testee.has_connection('aa', 'bb')
    assert testee.has_connection('bb', 'cc')
    assert set(testee.find_triples()) == set(['aa,bb,cc'])


def test_find_two_networks_of_three():
    testee = Network('aa-bb\naa-dd\naa-cc\ncc-bb\naa-ta\nta-cc')
    assert set(testee.find_triples()) == set(['aa,bb,cc','aa,cc,ta'])
    