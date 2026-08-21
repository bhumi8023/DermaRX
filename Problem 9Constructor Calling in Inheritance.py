class Person:
    def __init__(self,name):
        print("Hi i am a base class")
        self.name = name

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        print("I am a derived class")

s1 = Student("bhumi")
s1.name
    
        