from lib.cohort import Cohort
from lib.cohort_repository import CohortRepository
from lib.student import Student


# def test_returns_all(db_connection):
#     db_connection.seed("seeds/student_directory.sql")
#     cohort_repository = CohortRepository(db_connection)
#     assert cohort_repository.all() == [
#         Cohort(1, 'Cohort A', '2022-01-01'),
#         Cohort(2, 'Cohort B', '2022-02-01'),
#         Cohort(3, 'Cohort C', '2022-03-01')
#     ]

def test_returns_all(db_connection):
    db_connection.seed("seeds/student_directory.sql")
    cohort_repository = CohortRepository(db_connection)
    assert cohort_repository.all() == [
        Cohort(1, 'Cohort A', '2022-01-01'),
        Cohort(2, 'Cohort B', '2022-02-01'),
        Cohort(3, 'Cohort C', '2022-03-01')
    ]

def test_find_cohort_with_students(db_connection):
    db_connection.seed("seeds/student_directory.sql")
    cohort_repository = CohortRepository(db_connection)
    assert cohort_repository.find_cohort_with_students(3) == Cohort(3, 'Cohort C', '2022-03-01', [
            Student(4, 'Alice Williams', 3),
            Student(7, 'Sophia Lee', 3),
            Student(10, 'William Wilson', 3),
            Student(13, 'Ava Moore', 3)
        ])