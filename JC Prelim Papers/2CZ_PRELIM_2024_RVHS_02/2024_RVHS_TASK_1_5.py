# task 1.5
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/available/<date>')
def avail(date):
    con = sqlite3.connect("cu_booking.db")
    c = con.cursor()

    cub_query = "SELECT c.cubicle_no FROM cubicle c"

    c.execute(cub_query)
    cubicles = [i[0] for i in c.fetchall()]

    avail_query = "SELECT c.cubicle_no FROM cubicle c LEFT OUTER JOIN booking b ON c.cubicle_no = b.cubicle_no AND b.date = ? WHERE c.maintenance = 0 AND b.cubicle_no is NULL"

    c.execute(avail_query,(date,))
    avail_cub = [i[0] for i in c.fetchall()]

    avails = [(i,"Unavailable") if i not in avail_cub else (i,"Available") for i in cubicles]

    return render_template("index.html",date=date,avails=avails)


app.run()
