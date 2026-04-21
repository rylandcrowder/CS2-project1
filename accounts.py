
class Account:
    def __init__(self, name, balance=0):
        self.__account_name = name
        self.__account_balance = balance
        self.set_balance(self.__account_balance)

    def deposit(self, amount):
        try:  
            if (amount > 0):
                new_balance = self.__account_balance + amount
                self.set_balance(new_balance)
                return True
            else: 
                return False
        except: 
            return False
    def withdraw(self, amount):
        if self.__account_balance >= amount > 0:
            new_balance = self.__account_balance - amount
            self.set_balance(new_balance)
            return True
        else:
            return False
    def get_balance(self):
        return self.__account_balance
    
    def get_name(self):
        return self.__account_name
    
    def set_balance(self, value):
        if value > 0:
            self.__account_balance = value
        else:
            self.__account_balance = 0
    def set_name(self, value):
        self.__account_name = value

    def __str__(self):
        return f'Account name = {self.get_name()}, Account balance = {self.get_balance():.2f}'
    
class SavingAccount(Account):
    def __init__(self,name):
        minimum = 100
        rate = 0.02
        
        self.__minimum = minimum 
        self.__rate = rate 
        self.__deposit_count = 0
        super().__init__(name, balance = self.__minimum)
    def apply_interest(self):
        if (self.__deposit_count % 5 == 0):
            new_balance = self.get_balance() * (1 + self.__rate)
            self.set_balance(new_balance)
    def deposit(self, amount):
        try:
            if super().deposit(amount):
                self.__deposit_count += 1
                self.apply_interest()
                return True
            else:
                return False
        except:
            return False

    def withdraw(self, amount):
        if (self.get_balance() - self.__minimum >= amount > 0):
            return super().withdraw(amount)
        else:
            return False
    def set_balance(self, value):
        if value > self.__minimum:
            super().set_balance(value)
        else:
            super().set_balance(self.__minimum)

    def __str__(self):
        return f'SAVING ACCOUNT: {super().__str__()}'