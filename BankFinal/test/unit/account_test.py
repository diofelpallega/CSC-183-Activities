import unittest
from bank.account import Account
from bank.account import AccountWithdraw


class TestAccount(unittest.TestCase):
    def test_account_object_can_be_created(self):
        account = Account("001",50)
        self.assertEqual(account.account_number,"001")
        self.assertEqual(account.balance,50)
    
    def test_account_object_returns_current_balance(self):        
        account = Account("001",50)
        self.assertEqual(account.account_number,"001")
        self.assertEqual(account.balance, 50)

    def test_account_object_can_withdraw(self):
        account = AccountWithdraw("001",50,5)
        self.assertEqual(account.balance,45)
    
        
if __name__== '__main__':
    unittest.main()
