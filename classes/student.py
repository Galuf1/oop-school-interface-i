from classes.person import Person
import csv

class Student(Person):
    def __init__(self, name, age, role, password, school_id):
        Person.__init__(self, name, age, role, password)
        self.school_id = school_id

    def all_students(self):
        students_array = []
        students_file = csv.DictReader(open("data/students.csv"))
        for row in students_file:
            students_array.append(row)
        return students_array