class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance-=amount

    def deposit(self, amount):
        self.balance+=amount
        
    def getBalance(self):
         return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        self.intamount=(self.interestRate*self.balance)/100
        return self.intamount
    def get_Details(self):
         print(f'\nName:-{self.title}\nBalance{self.balance}\nInterest Rate:-{self.interestRate}\n')
         
    

acc=SavingsAccount()
