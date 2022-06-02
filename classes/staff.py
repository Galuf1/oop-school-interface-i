from classes.person import Person
import csv

class Staff(Person):
    def __init__(self, name, age, role, password, employee_id):
        Person.__init__(self, name, age, role, password)
        self.employee_id = employee_id
    
    def all_staff(self):
        staff_array = []
        staff_file = csv.DictReader(open("data/staff.csv"))
        for row in staff_file:
            staff_array.append(row)
        return staff_array

        