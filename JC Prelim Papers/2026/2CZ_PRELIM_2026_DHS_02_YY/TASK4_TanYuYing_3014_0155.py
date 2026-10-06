from flask import Flask, render_template, request 

from pymongo import MongoClient 

import json 

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"]) 
def home(): 

    with open("prelim_results.json") as f: 
        prelim_info = json.load(f) 

    client = MongoClient("localhost",27017) 

    db = client["DHS"] 

    coll = db["Prelims"] 

    coll.delete_many({}) 

    coll.insert_many(prelim_info)

    prelim_data = list(coll.find()) 

    results = [] 

    student_list = [] 

    for data in prelim_data: 
        one_result = [data["student_id"],data["full_name"]] 

        for subject in data["results"].keys(): 
            one_result.append(subject) 
            one_result.append(data["results"][subject]) 

        results.append(one_result)

        student_list.append(data["full_name"]) 

    if request.method == "POST": 
        student_name = request.form.get("student_name") 

        student_prelim_info = coll.find_one({"full_name":student_name}) 

        student_result = [student_prelim_info["student_id"],student_prelim_info["full_name"]]

        for subject in student_prelim_info["results"].keys(): 
            student_result.append(subject) 
            student_result.append(student_prelim_info["results"][subject]) 

        results = [student_result] 

    return render_template("index.html",results=results,student_list = student_list) 

app.run() 

    
    