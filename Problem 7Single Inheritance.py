class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, rollno):
        super().__init__(name, age)
        self.rollno = rollno

s1 = Student("bhumi", 10, 101)
# s1.age = 10
# s1.name = "bhumi"
# s1.rollno = 101
print(s1.name)
print(s1.age)
print(s1.rollno)

