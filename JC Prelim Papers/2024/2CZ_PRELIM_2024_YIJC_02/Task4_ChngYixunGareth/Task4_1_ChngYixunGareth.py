# task 4.1
import csv
import sqlite3

with open("Q4_webapp/PURCHASE.TXT") as f:
    data = [i for i in csv.reader(f)][1:]

con = sqlite3.connect("Q4_webapp/LOYALTY.db")
c = con.cursor()
c.execute("DELETE FROM Purchase")
c.executemany("INSERT INTO Purchase(ConcertID,Email,Quantity) VALUES (?,?,?)",data)
con.commit()
con.close()