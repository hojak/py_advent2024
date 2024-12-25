from day22.tools import mix_in

import pytest


@pytest.mark.parametrize('a, b, expected', [
    (3,5,6),
    (2,10,8),
    (15,42,37),
])
def test_mix_in(a, b, expected):   
    assert mix_in(a, b) == expected