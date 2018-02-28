from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'MySecretKey'

@app.route('/')
def index():
    if 'random_number' not in session:
        session['random_number'] = random.randrange(0,101)
    if 'number_of_guesses' not in session:
        session['number_of_guesses'] = 0
    if 'state' not in session:
        session['state'] = "empty"
    if 'user_guess' not in session:
        session['user_guess'] = 0
    if 'current_guesses' not in session:
        session['current_guesses'] = ""
    return render_template('index.html')

@app.route('/process', methods=['post'])
def process():
    session['number_of_guesses'] += 1
    session['current_guesses'] += str(request.form['user_guess']) + ", "
    session['user_guess'] = request.form['user_guess']
    if int(session['user_guess']) == session['random_number']:
        session['state'] = "won"
    if int(session['user_guess']) < session['random_number']:
        session['state'] = "low"
    if int(session['user_guess']) > session['random_number']:
        session['state'] = "high"
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['random_number'] = random.randrange(0,101)
    session['number_of_guesses'] = 0
    session['state'] = "empty"
    session['user_guess'] = 0
    session['current_guesses'] = ""
    return redirect('/')

app.run(debug=True)
