from day2.report_checks import is_save

import pytest

@pytest.mark.parametrize('list_of_levels, expected', [
    ([], True),
    ([1], True),
    ([1,3], True),
    ([1,3,2], False),
    ([3,2,1], True),
    ([3,1,2], False),
    ([1,4,7], True),
    ([1,5,7], False),
    ([1,2,2], False),
    ([10,8,5], True),
    ([10,8,4], False),
])
def test_is_save(list_of_levels: list, expected:bool) -> None:
    assert is_save(list_of_levels) == expected