from flask import Flask, request,render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload',methods=["POST"])
def upload():
    if request:
        file = request.files.get("image")
        file.save(f"./static/images/{secure_filename(file.filename)}")
    return render_template("index.html",image=f"images/{file.filename}")
    
app.run(debug=True)