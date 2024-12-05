import pytest

from day5.ReleaseRequirements import ReleaseRequirements

# @pytest.mark.parametrize('init_str, expected_width', [
#     ('X', 1),
#     ('XM\nAS', 2),
#     ('XMA\nAXM', 3),
# ])
def test_requirements_init_updates() -> None:
    testee = ReleaseRequirements('''10|12
                                 
11,12
12,7,10''')
    assert len(testee.get_updates()) == 2

@pytest.mark.parametrize('init_str, expected_requirements', [
    ('''10|12
                                 
11,12''', {12: [10]}),
    ('''11|12
10|12
10|13
                                 
11,12''', {12: [11,10], 13: [10]}),
])
def test_requirements_init_updates(init_str, expected_requirements) -> None:
    testee = ReleaseRequirements(init_str)
    assert testee.requirements == expected_requirements
