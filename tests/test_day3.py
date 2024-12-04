from day3.tools import find_mul_statements, get_mul_result, get_program_result

import pytest

@pytest.mark.parametrize('input, expectedFindings', [
    ('mul(1,1)', ['mul(1,1)']),
    ('mul(123,1)', ['mul(123,1)']),
    ('mul(1,123)', ['mul(1,123)']),
    ('mul(1234,1)', []),
    ('xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))', ['mul(2,4)', 'mul(5,5)', 'mul(11,8)','mul(8,5)'])
])
def test_find_mul_statements(input: str, expectedFindings:list) -> None:
    assert find_mul_statements(input) == expectedFindings

@pytest.mark.parametrize('input, expectedValue', [
    ('mul(1,1)', 1),
    ('mul(123,1)', 123),
    ('mul(2,123)', 246),
    ('q93824e98124', 0)
])
def test_get_mul_result(input: str, expectedValue:int) -> None:
    assert get_mul_result(input) == expectedValue

def test_get_program_result() -> None:
    assert get_program_result ('xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))') == 161

