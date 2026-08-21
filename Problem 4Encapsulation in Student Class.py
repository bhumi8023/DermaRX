class Student:
    
    def setmarks(self, marks):
        if(marks>=85):
            print("The grade is A")
        elif(marks>=70 and 85>marks):
            print("The grade is B")
        elif(70>marks and 55<=marks):
            print("The grade is C")
        else:
            print("The grade is D")

s1 = Student()    
s1.setmarks(85)

                              

    