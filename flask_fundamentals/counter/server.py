from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def home():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] +=1
    return render_template('index.html')

@app.route('/plus2', methods=['POST'])
def submit_button():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)