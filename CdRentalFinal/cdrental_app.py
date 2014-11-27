from cd import *
from clerk import *
from customers import *
from cds import *
from clerk import *
from flask import Flask

app = Flask(__name__)
customers = Customers()
cds = cds()



@app.route('/')
def hello_world():
    customer_id = request.args.get('customer_id')
    cd_id = request.args.get('cd_id')
    clerk = Clerk.checkout(customer_id,cd_id)
    return render_template('index.html', balance=balance)

if __name__ == '__main__':
    app.run(debug=True)

