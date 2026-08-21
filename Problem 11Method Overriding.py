class Person:
    def display(self):
        print("Hi i am a base class")
        

class Student(Person):
    def display(self):
        print("Hi i am a derived class")
    

s1 = Student()
s1.display()

    
        