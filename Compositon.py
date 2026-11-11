## it is a concept of designing a object of child class as a attribute in parent class
class Distrct:
    def __init__(self, name: str):
        self.name = name
        self.schools = []

    def add_school(self, school: 'School'):
        self.schools.append(school)

    def remove_school(self, school: 'School'):
        self.schools.remove(school)
        
class School:
    def __init__(self, name: str):
        self.name = name

    def add_school(self, school: 'School'):
        self.schools.append(school)

    def remove_school(self, school: 'School'):
        self.schools.remove(school)