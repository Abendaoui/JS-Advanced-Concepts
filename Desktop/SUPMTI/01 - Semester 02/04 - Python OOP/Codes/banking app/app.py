from bank_accounts import *
from interest_reward_acc import *
from saving_acc import *

adil = BankAccount(1200,'Adil')
hind = InterestRewardAcc(0,'Hind')
john = SavingAcc(1000,'John')


adil.transfer(100,hind)

adil.transaction_history()
hind.transaction_history()


