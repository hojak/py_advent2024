from day2.report_checks import is_save

import pytest

@pytest.mark.parametrize('list_of_levels, expected', [
    ([], True),
])

def test_is_save(list_of_levels: list, expected:bool) -> None:
    assert is_save(list_of_levels) == expected