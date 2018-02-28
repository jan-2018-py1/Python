from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import datetime
import re
import md5

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app,'login_registration')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    session.pop('_flashes', None)
    return redirect('/')

@app.route('/view')
def view():
    query = "SELECT * FROM users"                           
    users_list = mysql.query_db(query)                           
    return render_template('users.html', users=users_list) 

@app.route('/login', methods=['POST'])
def login():
    error = False
    hashed_password = md5.new(request.form['password']).hexdigest()
    query = "SELECT username, password FROM users WHERE username = :username"
    data = {
        'username': request.form['username']
    }                           
    username = mysql.query_db(query,data)

    if len(username) != 0:
        if username[0]['password'] != hashed_password:
            flash("Username or password is incorrect")
            return redirect('/')
        else:
            session['username'] = request.form['username']
            session['login_success'] = True
            session['register_success'] = False
            return redirect('/success')
    else:
        flash("Username or password is incorrect")
        return redirect('/')

@app.route('/success')
def success():         
    return render_template('success.html') 

@app.route('/register', methods=['POST'])
def process():
    error = False

    if len(request.form['first_name']) < 2:
        flash("First Name must be two or more letters")
        error = True
    elif request.form['first_name'].isalpha() == False:
        flash("First Name cannot contain numbers")
        error = True

    if len(request.form['last_name']) < 2:
        flash("Last Name must be two or more letters")
        error = True
    elif request.form['last_name'].isalpha() == False:
        flash("Last Name cannot contain numbers")
        error = True

    query = "SELECT username FROM users WHERE username = :username"
    data = {
        'username': request.form['username']
    }                           
    username = mysql.query_db(query, data)
    if len(username) != 0:
        flash(request.form['username'] + " has already been registered")
        error = True

    if len(request.form['email_address']) < 1:
        flash("Email Address cannot be blank")
        error = True
    elif not EMAIL_REGEX.match(request.form['email_address']):
        flash("Invalid Email Address")
        error = True

    if len(request.form['password']) < 1:
        flash("Password cannot be blank")
        error = True
    elif len(request.form['password']) < 8:
        flash("Password must be at least 8 characters")
        error = True
    elif not PASSWORD_REGEX.match(request.form['password']):
        flash("Invalid Password, must contain at least one uppercase and one number")
        error = True
    
    if len(request.form['confirm_password']) < 1:
        flash("Confirm Password cannot be blank")
        error = True 
    elif request.form['password'] != request.form['confirm_password']:
        flash("Passwords do not match")
        error = True

    if error == True:
        return redirect('/')
    if error == False:
        hashed_password = md5.new(request.form['password']).hexdigest()
        query = "INSERT INTO users (first_name, last_name, username, email_address, password, created_at) VALUES (:first_name, :last_name, :username, :email_address, :password, NOW())"    
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email_address': request.form['email_address'],
            'username': request.form['username'],
            'password': hashed_password,
        }
        mysql.query_db(query, data)
        flash(request.form['username'] + " was added to the system")
        
        session['username'] = request.form['username']
        session['register_success'] = True
        session['login_success'] = False

        return redirect('/success')

app.run(debug=True)
