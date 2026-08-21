class Calculator:

    def setnumber1(self,number1):
        self.number1 = number1

    def setnumber2(self,number2):
        self.number2 = number2  

    def addition(self):
        self.result = self.number1+self.number2
        return self.result

c1 = Calculator()
c1.setnumber1(25)
c1.setnumber2(80)
print(c1.addition())

