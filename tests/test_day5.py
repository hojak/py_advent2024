import pytest

from day5.ReleaseRequirements import ReleaseRequirements, get_middle_number



def test_requirements_init_updates ():
    testee = ReleaseRequirements('''10|12
                                 
11,12
12,7,10''')
    assert testee.updates == [[11,12], [12,7,10]]

@pytest.mark.parametrize('init_str, expected_requirements', [
    ('''10|12
                                 
11,12''', {12: [10]}),
    ('''11|12
10|12
10|13
                                 
11,12''', {12: [11,10], 13: [10]}),
])
def test_requirements_init_rules(init_str, expected_requirements) -> None:
    testee = ReleaseRequirements(init_str)
    assert testee.requirements == expected_requirements


def test_get_middle_number():
    assert get_middle_number([1,2,3,4,5]) == 3

@pytest.mark.parametrize('init_str, extected_validity', [
    ('''10|12
                                 
11,12''', True),
    ('''10|12
                                 
11,12,9,10,8''', False),
])
def test_is_valid ( init_str, extected_validity): 
    testee = ReleaseRequirements(init_str)
    assert testee.is_valid(testee.updates[0]) == extected_validity
