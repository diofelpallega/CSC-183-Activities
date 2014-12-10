"""DOCSTRING"""
from flask import Flask, render_template, request
from bank.account import Account
from bank.bank import Bank

APP = Flask(__name__)
BANK = Bank()

@APP.route('/')
def run_site():
    """run site"""
    account_number = request.args.get('account_number')
    balance = BANK.get_account_balance(account_number)
    return render_template('index.html', balance=balance)

if __name__ == '__main__':
    import cProfile

    ACCOUNT = Account('1111', 50)
    BANK.add_account(ACCOUNT)
    cProfile.run('APP.run(debug=True)', sort='time')







