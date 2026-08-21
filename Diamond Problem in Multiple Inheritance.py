class Person:
    def __init__(self):
        print("I am a person")
class Human(Person):
    def __init__(self):
        super().__init__()
        print("human......")

class Student(Person):
    def __init__(self):
        super().__init__()
        print("I am student")
class Athelete(Human,Student):
    pass      

c1 = Athelete()
