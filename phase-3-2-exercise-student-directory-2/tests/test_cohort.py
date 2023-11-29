from lib.cohort import Cohort

"""
constructs with values
"""

def test_construct_with_values():
    cohort = Cohort(1, 'Cohort A', '2023-10-30')
    assert cohort.id == 1
    assert cohort.name == 'Cohort A'
    assert cohort.start_date == '2023-10-30'

"""
has string representation
"""

def test_string_representation():
    cohort = Cohort(1, 'Cohort A', '2023-10-30')
    assert str(cohort) == "Cohort(1, Cohort A, 2023-10-30)"

"""
instances with same values are equal
"""

def test_instances_with_same_values_are_equal():
    cohort1 = Cohort(1, 'Cohort A', '2023-10-30')
    cohort2 = Cohort(1, 'Cohort A', '2023-10-30')
    assert cohort1 == cohort2