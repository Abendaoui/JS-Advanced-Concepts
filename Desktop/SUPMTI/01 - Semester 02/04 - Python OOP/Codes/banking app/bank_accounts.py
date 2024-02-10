from balance_exception import *
from instance_exception import *


class BankAccount:
    
    def __init__(self,initial_amount,acc_name):
        self.balance = initial_amount
        self.name = acc_name
        self.transaction_list = []
        
    def get_balance(self):
         print(f"Account '{self.name}'\nBalance : '${self.balance:.2f}'\n")
         
    def deposit(self, amount):
        self.balance += amount
        print('\nDeposit Complete.')
        self.get_balance()
        return True
    
    # Custom Exceptions
    def viable_transactions(self,amount):
        if(self.balance >= amount):
            return
        else:
            raise BalanceException(f'Sorry, Insufficient Balance In {self.name} Account\n')
    
    def validate_receiver(self,account):
        if isinstance(account,BankAccount):
            return
        else:
            raise InstanceException(f'The Receiver Account Is Not Valid BankAccount\n')
        
    def withdraw(self, amount):
        try:
            self.viable_transactions(amount)
            self.balance -= amount
            print('Withdraw Complete.')
            self.get_balance()
            return True
        except BalanceException as error:
            print(error)
    
    def transaction_history(self):
        if len(self.transaction_list) == 0:
            print('No Transaction History Found')
        else:
            for transaction in self.transaction_list:
                print('==>\t{} {} {} : ${}{}\n'.format(
                transaction['sender'], 
                transaction['access'], 
                transaction['receiver'], 
                transaction['sign'], 
                transaction['amount']
            ))
                
    def create_transaction(self,sender,receiver,amount,sign,access):
        self.transaction_list.append({'sender':sender, 'receiver': receiver, 'amount':str(amount), 'sign':sign, 'access':access})
                
    def transfer(self, amount,receiver):
            try:
                self.validate_receiver(receiver) # check
                if(self.withdraw(amount)):
                    receiver.deposit(amount)
                    print('Transfer Complete.\n')
                self.create_transaction(self.name,receiver.name,amount,'-','-->')
                receiver.create_transaction(receiver.name,self.name,amount,'+','<--')
            except InstanceException as error:
                print(error)
        
