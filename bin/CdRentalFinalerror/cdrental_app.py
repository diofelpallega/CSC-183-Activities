from cd.cd import *
from cd.clerk import *
from cd.customers import *
from cd.cds import *
from cd.clerk import *
from flask import Flask, render_template,request

app = Flask(__name__)
 


@app.route('/')
def visit_homepage():
    customer_id = request.args.get('customer_id')
    cd_id = request.args.get('cd_id')
    clerk = Clerk(Customers(),Cds())
    result = clerk.checkout(customer_id,cd_id)
    return render_template('index.html', output=result)
    
if __name__ == '__main__': 
    app.run(debug=True)

