import  random


class Account:
    def __init__(self):
        self.account_number =self.generate_account_number()
        self.balance = 1000
    
    def generate_account_number(self):
        digits = '0123456789'
        account_number = ''
        for _ in range(10):
            account_number += random.choice(digits)
        return account_number
       
    
    def check_balance(self):
        #self.account_number =self.generate_account_number()
        #self.balance = 1000
        return self.balance
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False
    
    
    
    