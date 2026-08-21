class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, rollno):
        super().__init__(name, age)
        self.rollno = rollno

class GraduateStudent(Student):
    def __init__(self, name, age, rollno,collegename):
        super().__init__(name, age,rollno)
        self.collegename = collegename

s1 = GraduateStudent("bhumi",10,101,"sage")
print(s1.name)
print(s1.age)
print(s1.rollno)
print(s1.collegename)

