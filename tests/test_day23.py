from day23.Network import Network
import pytest


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
    

def test_find_only_tripels_with_a_t_computer():
    testee = Network('aa-bb\naa-dd\naa-cc\ncc-bb\naa-ta\nta-cc')
    assert set(testee.find_triples_with_t_computer()) == set(['aa,cc,ta'])



@pytest.mark.parametrize('network, expected_max_clique', [    
    ('aa-bb\naa-cc\naa-dd\naa-ee\nbb-cc\nbb-dd\nbb-ee\ncc-dd\ncc-ee\ndd-ee\n', 'aa,bb,cc,dd,ee'),
    ('aa-bb\naa-cc\naa-dd\naa-ee\nbb-cc\nbb-dd\nbb-ee\ncc-dd\ncc-ee\ndd-ee\naa-zz\nbb-zz\ncc-dd\nee-xy', 'aa,bb,cc,dd,ee')
])
def test_find_max_clique(network, expected_max_clique):
    testee = Network(network)
    assert testee.find_max_clique() == expected_max_clique
    

