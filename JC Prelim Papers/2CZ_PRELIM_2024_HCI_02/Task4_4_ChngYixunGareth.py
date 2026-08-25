from flask import Flask, render_template,request
import sqlite3

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    data = {
        "valid":False
    }

    if request.method == 'POST':
        date = request.form.get('date')
        con = sqlite3.connect("TRIP.db")
        c = con.cursor()

        c.execute("""
            SELECT c.Name,f.DepartCity,f.ArrivalCity,t.Seat 
            FROM Ticket t 
            JOIN Flight f ON f.FlightNo = t.FlightNo 
            JOIN Customer c ON c.CustomerNo = t.CustomerNo 
            WHERE t.Date = ?
        """,(date,)
        )

        data["date"] = date
        data["data"] = list(c.fetchall())
        print(c.fetchall())
        data["valid"] = True

    return render_template("index.html",info = data)


app.run(debug=True)