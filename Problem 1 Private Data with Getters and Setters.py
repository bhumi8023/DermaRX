class Student:
    
    def get_name(self):    
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):    
        return self.age

    def set_age(self, age):
        self.age = age 

s1 = Student()
s1.set_name("Alice")
s1.set_age(20)

print("The student name is:",s1.get_name())
print("The student age is:",s1.get_age())

