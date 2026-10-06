from pymongo import MongoClient
from flask import Flask,render_template,request

def parse(student):
    parsed = [
        student["student_id"],
        student["full_name"]
    ] + sum([
        list(i) for i in student["results"].items()
    ],[])

    return parsed

def get_results(student=None):
    client = MongoClient()
    db = client["DHS"]
    coll = db["Prelims"]

    query_doc = {"full_name": student} if student is not None else {}
    data = coll.find(query_doc,{"_id":0})

    parsed_data = [parse(i) for i in list(data)]
    return parsed_data

def get_namelist():
    client = MongoClient()
    db = client["DHS"]
    coll = db["Prelims"]
    data = coll.find({},{"full_name":1,"_id":0})
    return [i["full_name"] for i in list(data)]

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    namelist = get_namelist()
    name = request.form.get("student")
    if name not in namelist:
        name = None
    return render_template("index.html",namelist=namelist, results = get_results(name))


app.run()