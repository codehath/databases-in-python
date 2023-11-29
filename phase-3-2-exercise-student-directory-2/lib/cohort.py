class Cohort:
    def __init__(self, id, name, start_date, students = []):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.students = students

    def __repr__ (self):
        return f"Cohort({self.id}, {self.name}, {self.start_date})"
    
    def __eq__ (self, other):
        return self.__dict__ == other.__dict__
    