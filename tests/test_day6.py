import pytest

from day6.LabMap import LabMap

@pytest.mark.parametrize('init_str, expected_width', [
    ('''....
....
....''', 4),
])
def test_width(init_str, expected_width) -> None:
    testee = LabMap(init_str)
    assert testee.get_width() == expected_width


