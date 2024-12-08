import pytest

from day8.AntennaMap import AntennaMap



@pytest.mark.parametrize('input, expected_frequencies', [
    ('A', ['A']),
    ('ABAAB', ['A', 'B']),
])
def test_finding_frequencies(input, expected_frequencies) -> None:
    testee = AntennaMap(input)
    assert testee.get_found_frequencies() == expected_frequencies    
