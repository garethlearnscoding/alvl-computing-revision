from flask import Flask,render_template

app = Flask(__name__)


data = [1,2,3,4,5,6,7,8,9,10]

@app.route('/')
def index():
    return render_template("index.html",timeline = data)

app.run(debug=True)


