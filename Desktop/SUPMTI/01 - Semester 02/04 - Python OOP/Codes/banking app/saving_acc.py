from interest_reward_acc import *
from balance_exception import *

class SavingAcc(InterestRewardAcc):
    def __init__(self, initial_amount, acc_name):
        super().__init__(initial_amount, acc_name)
        self.fee = 5
        
    def withdraw(self, amount):
        try:
            self.viable_transactions(amount + self.fee)
            self.balance -= amount + self.fee
            print('Withdraw Complete.')
            self.get_balance()
            return True
        except BalanceException as error:
            print(error)
        
        
