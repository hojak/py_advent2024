from day3.tools import find_all_statements, get_mul_result, get_multiplication_results, get_program_result

import pytest

@pytest.mark.parametrize('input, expectedFindings', [
    ('mul(1,1)', ['mul(1,1)']),
    ('mul(123,1)', ['mul(123,1)']),
    ('mul(1,123)', ['mul(1,123)']),
    ('mul(1234,1)', []),
    ('xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))', ['mul(2,4)', 'mul(5,5)', 'mul(11,8)','mul(8,5)']),
    ('xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5)))', ['mul(2,4)','don\'t()','mul(5,5)','mul(11,8)','do()','mul(8,5)'])
])
def test_find_all_statements(input: str, expectedFindings:list) -> None:
    assert find_all_statements(input) == expectedFindings

@pytest.mark.parametrize('input, expectedValue', [
    ('mul(1,1)', 1),
    ('mul(123,1)', 123),
    ('mul(2,123)', 246),
    ('q93824e98124', 0)
])
def test_get_mul_result(input: str, expectedValue:int) -> None:
    assert get_mul_result(input) == expectedValue

def test_get_multiplication_results() -> None:
    assert get_multiplication_results ('xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))') == 161

def test_get_program_result() -> None:
    assert get_program_result ( 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))') == 48 