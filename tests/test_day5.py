import pytest

from day5.ReleaseRequirements import ReleaseRequirements



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
