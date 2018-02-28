from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    ninjas = "img/tmnt.png"
    ninja_name = "Teenage Mutant Ninja Turtles"
    return render_template("ninja.html", image=ninjas, name=ninja_name)

@app.route('/ninja/<color>')
def ninja_color(color):
    ninja = "img/notapril.jpg"
    ninja_name = "April"
    if color == "blue":
        ninja = "img/leonardo.jpg"
        ninja_name = "Leonardo"
    elif color == "orange":
        ninja = "img/michelangelo.jpg"
        ninja_name = "Michelangelo"
    elif color == "red":
        ninja = "img/raphael.jpg"
        ninja_name = "Raphael"
    elif color == "purple":
        ninja = "img/donatello.jpg"
        ninja_name = "Donatello"
    return render_template("ninja.html", image=ninja, name=ninja_name)

app.run(debug=True)