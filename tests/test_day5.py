import pytest

from day5.ReleaseRequirements import ReleaseRequirements, get_middle_number



def test_requirements_init_updates ():
    testee = ReleaseRequirements('''10|12
                                 
11,12
12,7,10''')
    assert testee.updates == [[11,12], [12,7,10]]

@pytest.mark.parametrize('init_str, expected_requirements', [
    ('''10|12
                                 
11,12''', {12: [10]}),
    ('''11|12
10|12
10|13
                                 
11,12''', {12: [11,10], 13: [10]}),
])
def test_requirements_init_rules(init_str, expected_requirements) -> None:
    testee = ReleaseRequirements(init_str)
    assert testee.requirements == expected_requirements


def test_get_middle_number():
    assert get_middle_number([1,2,3,4,5]) == 3

@pytest.mark.parametrize('init_str, extected_validity', [
    ('''10|12
                                 
11,12''', True),
    ('''10|12
                                 
11,12,9,10,8''', False),
])
def test_is_valid ( init_str, extected_validity): 
    testee = ReleaseRequirements(init_str)
    assert testee.is_valid(testee.updates[0]) == extected_validity

@pytest.mark.parametrize('init_str, expected_result', [
    ('''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47''', 143)
])
def test_get_middle_number(init_str, expected_result):
    testee = ReleaseRequirements(init_str)
    assert testee.get_sum_for_valid_updates() == expected_result



@pytest.mark.parametrize('update, expected_fix', [
    ([75,97,47,61,53], [97,75,47,61,53]),
    ([61,13,29],[61,29,13]),
    ([97,13,75,29,47], [97,75,47,29,13]),
])
def test_get_fix(update, expected_fix):
    testee = ReleaseRequirements('''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75''')
    assert testee.get_fix(update) == expected_fix    