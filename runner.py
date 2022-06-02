from classes.school import School
from classes.student import Student
from classes.staff import Staff 

school = School('Ridgemont High') 

print(school.name)
# diana = Student('Diana', 17, 'password', 'Student', 12345)
# diana = Student(school_id=12345, age=17, password='password', role='Student',  name='Diana')
student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
diana = Student(**student_info)
print(diana.role)
diana.all_students()
print(school.students)
print(school.staff)



'''
- import the csv
- create classes and subclasses
- import the school class
- 
'''