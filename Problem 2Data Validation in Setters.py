class Bank:
    # def __init__(self, balance):
    #     self.balance = balance

    def set_balance(self,balance):
        self.balance = balance
        if(balance<0):
            print("Invalid balance")
        else:
            print("Balance is unchanged")
    def get_balance(self): #self represent object thet define ss
        return self.balance

b1 = Bank()
b1.set_balance(-100)

        
            