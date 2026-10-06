# task 4.4
from flask import Flask,render_template
import sqlite3

app = Flask(__name__)


# team_name: [char_name,event_name,score]

def data():
    con = sqlite3.connect("esports.db")
    c = con.cursor()

    c.execute("""
        SELECT TeamName,CharacterName,EventName,Score FROM PLAYER ORDER BY TeamName, Score DESC
    """)

    data = list(c.fetchall())
    data_dict = {}

    for i in data:
        if i[0] not in data_dict.keys():
            data_dict[i[0]] = [i[1:]]
        else:
            data_dict[i[0]] += [i[1:]]

    return data_dict

data_dict = data()

@app.route('/')
def index():
    teams = data_dict.keys()
    return render_template("index.html",teams = teams)

@app.route('/<team_name>')
def team(team_name):
    members = data_dict[team_name]
    print(members)
    return render_template("team.html",members = members)

app.run(debug=True)