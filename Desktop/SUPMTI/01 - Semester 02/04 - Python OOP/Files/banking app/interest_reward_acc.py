from bank_accounts import *


class InterestRewardAcc(BankAccount):
    
    #OverRide
    def deposit(self, amount):
        self.balance += amount * 1.05
        print('\nDeposit Complete.')
        self.get_balance()
        return True
