from flask import Flask, render_template, request, redirect, url_for, json, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['post'])
def process():
    ninja = ""
    data = request.form["color"]

    if data == "red":
        ninja = "Raphael"
        image_path = "static/img/raphael.jpg"
    elif data == "blue":
        ninja = "Leonardo"
        image_path = "static/img/leonardo.jpg"
    elif data == "orange":
        ninja = "Michelangelo"
        image_path = "static/img/michelangelo.jpg"
    elif data == "purple":
        ninja = "Donatello"
        image_path = "static/img/donatello.jpg"
    else:
        ninja = 'April'
        image_path = "static/img/notapril.jpg"

    return jsonify(name=ninja, file_path=image_path, color=data)

app.run(debug=True)