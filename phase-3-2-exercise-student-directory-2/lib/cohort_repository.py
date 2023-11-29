from lib.cohort import Cohort
from lib.student import Student

class CohortRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM cohorts')
        cohorts = [
            Cohort(row['id'], row['name'], row['starting_date']) for row in rows
            ]
        return cohorts
    
    def find_cohort_with_students(self, cohort_id):
        rows = self.connection.execute(
            "SELECT cohorts.id AS cohort_id, cohorts.name as cohort_name, cohorts.starting_date, students.id AS student_id, students.name as student_name, students.cohort_id " \
            "FROM cohorts JOIN students ON students.cohort_id = cohorts.id " \
            'WHERE cohorts.id = %s', [cohort_id])
        students = []
        for row in rows:
            student = Student(row['student_id'], row['student_name'], row['cohort_id'])
            students.append(student)
        
        return Cohort(rows[0]['cohort_id'], rows[0]['cohort_name'], rows[0]['starting_date'], students)