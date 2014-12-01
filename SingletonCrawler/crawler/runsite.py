from flask import Flask, render_template
app = Flask("site for crawler")

@app.route('/')
def index():
    return render_template('site.html')

if __name__=="__main__":
    app.run(debug=True)