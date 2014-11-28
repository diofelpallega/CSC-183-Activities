
class Account(object):
    def __init__(self, account_number, balance): 
            self.account_number = account_number
            self.balance = balance
       
 
class AccountWithdraw(object):
    def __init__(self, account_number, balance, withdraw_amount): 
            self.balance = balance - withdraw_amount 
     
