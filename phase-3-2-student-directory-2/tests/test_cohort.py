class Student:
    def __init__(self, id, name, cohort_id):
        self.id = id
        self.name = name
        self.cohort_id = cohort_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Student(id={self.id}, name={self.name}, cohort_id={self.cohort_id})"
    
class TestStudent:
    def test_student_constructor(self):
        student = Student(1, "John", 3)
        assert student.id == 1
        assert student.name == "John"
        assert student.cohort_id == 3