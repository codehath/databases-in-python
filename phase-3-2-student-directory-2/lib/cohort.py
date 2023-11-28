class Cohort:
    def __init__(self, id, name, starting_date, students = []):
        self.id = id
        self.name = name
        self.starting_date = starting_date
        self.students = students

    def __repr__ (self):
        return f"Cohort(id={self.id}, name={self.name}, starting_date={self.starting_date})"
    
    def __eq__ (self, other):
        return self.__dict__ == other.__dict__
    