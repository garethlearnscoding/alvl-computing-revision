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


@app.route('/booking')
def booking():
    con = connect("LOYALTY.db")
    c = con.cursor()
    c.execute("SELECT ConcertName FROM Concert")
    data = [i[0] for i in list(c.fetchall())]
    con.close()
    return render_template("booking.html",concert_data =data)


@app.route('/check',methods=["POST"])
def check():
    email = request.form["email"]
    pwd = request.form["pwd"]
    concert = request.form["concert"]
    tix = request.form["tix"]
    con = connect("LOYALTY.db")
    c = con.cursor()
    c.execute("SELECT MemberName,Password FROM Member WHERE Email = ?",(email,))
    data = c.fetchone()
    if data is None:
        data = False
        return render_template("success.html",valid = data)

    name,acc_pwd = c.fetchone()[0]
    if pwd != acc_pwd:
        data = False
        return render_template("success.html",valid = data)
    c.execute("SELECT ConcertID,Artiste,Price FROM Concert WHERE ConcertName = ?",(concert,))
    cID,artiste,p = c.fetchone()[0]
    c.execute("UPDATE Concert SET Quantity = Quantity - ? WHERE ConcertName = ?",(tix,concert))
    c.execute("INSERT INTO Purchase(ConcertID,Email,Quantity) VALUES (?,?,?)",(cID,email,tix))
    data = {
        "name":name,
        "email":email,
        "show":concert,
        "Artiste": artiste,
        "qty":tix,
        "price":p,
        "total":int(p)*int(tix)
    }
    return render_template("success.html",valid = data)



### Your code goes above this line##

app.run(debug=True, port = 5000)
