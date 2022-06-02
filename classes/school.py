from classes.student import Student
from classes.staff import Staff

class School(Student,Staff):
    def __init__(self,name):
        self.name = name
        self.staff = Staff.all_staff(self)
        self.students = Student.all_students(self)
        
