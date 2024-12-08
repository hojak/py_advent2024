import pytest

from day7.tools import is_reachable

@pytest.mark.parametrize('target, numbers, expected_result', [
    (10, [10], True),
    (10, [11], False),
])
def test_is_reachable(target, numbers, expected_result) -> None:
    assert is_reachable(target, numbers) == expected_result