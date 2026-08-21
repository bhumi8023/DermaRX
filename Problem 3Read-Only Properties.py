class Employee:

    def __init__(self,id):
        self.id = id

    def get_id(self):
        return self.id

e1 = Employee(100)
e1.get_id()

print("Employee id is:",e1.get_id())