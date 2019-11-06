#trial
class Account:
    interest= 0.02
    def _init_ (self, account_holder):
        self.account_holder=account_holder
        self.balance = 0
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if amount>self.balance:
            return 'insufficient funds'
        self.balance-=amount
        return self.balance

class CheckingAccount(Account):
    interest=0.01
    withdraw_fee=1
    def withdraw(self.amount):
        return Account.withdraw(self,amount+withdraw_fee)
