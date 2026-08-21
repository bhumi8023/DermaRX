class Employee: 

    # def __init__(self, name, salary): 
    #     self.name = name
    #     self.__salary = salary

    #def __init__(self):
    #     self.name = ""
    #     self.__salary = ""

    def get_name(self):    #self is object that is made 
        return self.name

    def set_name(self, name):
        self.name = name

    def setsalary(self,salary):
        self.__salary = salary    

    def getsalary(self):
        return self.__salary    

        #print("The salary is:",self.__salary)
        #self._salary = salary #this __ is used for private and one _ it become protected 
           
    # def displaydetails(self):
    #     print("The name of employee is:",e1.name)
    #     print("The salary is:",e1.__salary)

e1 = Employee()
#e1.__init__("XYZ1",120001)

e1.set_name("XYZ1")
e1.setsalary(12001)

e1.age=12

print("Employee age is:",e1.age)

print("Employee name is:",e1.get_name())
print("Employee salary is:",e1.getsalary())

#e1.displaydetails()

#print("The name of employee is:",e1.name)
#print("The salary is:",e1._salary)
