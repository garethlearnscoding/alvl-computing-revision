from sqlite3 import *


from flask import Flask, render_template, request
app = Flask(__name__) 

### Your code goes below this line##
@app.route('/')
def index():
    con = connect("LOYALTY.db")
    c = con.cursor()
    c.execute("""
        SELECT ConcertName,Artiste,Date,Price,Quantity FROM Concert
    """)
    data = list(c.fetchall())
    con.close()
    return render_template("index.html",data = data)









### Your code goes above this line##

app.run(debug=True, port = 5000)
