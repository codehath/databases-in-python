from lib.student import Student

def test_student_constructor(self):
    student = Student(1, "John Smith", 3)
    assert student.id == 1
    assert student.name == "John"
    assert student.cohort_id == 3

def test_student_equality(self):
    student1 = Student(1, "John Smith", 3)
    student2 = Student(1, "John Smith", 3)
    assert student1 == student2

def test_student_repr(self):
    student = Student(1, "John Smith", 3)
    assert repr(student) == "Student(1, John Smith, Cohort ID = 3)"