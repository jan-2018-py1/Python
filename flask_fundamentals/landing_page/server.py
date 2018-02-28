from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")

@app.route('/dojos/new', methods=["GET"])
def dojos():
    return render_template("dojos.html")
    name = request.form["name"]
    email = request.form["email"]

app.run(debug=True)