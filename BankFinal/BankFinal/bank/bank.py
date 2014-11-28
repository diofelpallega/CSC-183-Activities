class Bank(object):
    def __init__(self):
        self.accounts = {}
    
    def add_account(self, account):            
            self.accounts[account.account_number] = account.balance 

    def get_account_balance(self, account_number): 
            return self.accounts.get(account_number) 

    def withdraw_amount(self, account_number, amount): 
            wait_value =  self.accounts.get(account_number) 
            new_value = wait_value - amount
            return new_value 
