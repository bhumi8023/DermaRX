class Student:
    def __init__(self,name):
        self.name = name
        print("i am a student")

class Athelete:
    def __init__(self,sports):
        self.sports = sports
        print("I am a athelete")

class StudentAthelete(Student,Athelete):
    def __init__(self,name,sports,age):
        super().__init__(name)
      
        Athelete.__init__(self,sports)
        self.age = age
        

s1 = StudentAthelete("Bhumi","Badminton",5)
print(s1.name)
print(s1.sports)
print(s1.age)