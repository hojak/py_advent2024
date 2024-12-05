import pytest

from day5.ReleaseRequirements import ReleaseRequirements

# @pytest.mark.parametrize('init_str, expected_width', [
#     ('X', 1),
#     ('XM\nAS', 2),
#     ('XMA\nAXM', 3),
# ])
def test_requirements_init() -> None:
    testee = ReleaseRequirements('''10|12
                                 
11,12
12,7,10''')
    assert len(testee.get_rules()) == 1
    assert len(testee.get_updates()) == 2
