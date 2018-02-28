from flask import Flask, render_template, request, redirect, session
import random
import math
from time import gmtime, strftime

app = Flask(__name__)
app.secret_key = 'MySecretKey'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = []
    if 'sign' not in session:
        session['sign'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    temp = 0
    string = ""
    time = strftime("%c",gmtime())
    if request.form['location'] == 'farm':
        temp =random.randrange(10,21)
        string = "You got " + str(temp) + " gold pieces from the farm! (" + str(time) + ")"
    if request.form['location'] == 'cave':
        temp =random.randrange(5,11)
        string = "You got " + str(temp) + " gold pieces from the cave! (" + str(time) + ")"
    if request.form['location'] == 'house':
        temp =random.randrange(2,6)
        string = "You got " + str(temp) + " gold pieces from the house! (" + str(time) + ")"
    if request.form['location'] == 'casino':
        temp =random.randrange(-50,51)
        if temp < 0:
            string = "You lost " + str(int(math.fabs(temp))) + " gold pieces from the casino! (" + str(time) + ")"
        if temp >= 0:
            string = "You got " + str(temp) + " gold pieces from the casino! (" + str(time) + ")"
    session['gold'] += temp
    session['activity'].append(string)
    if temp < 0:
        session['sign'].append(False)
    if temp >= 0:
        session['sign'].append(True)
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['gold'] = 0
    session['activity'] = []
    session['sign'] = []
    return redirect('/')

app.run(debug=True)
