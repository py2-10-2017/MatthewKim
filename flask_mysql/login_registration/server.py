from flask import Flask, redirect, render_template, request, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import MySQLConnector
import re, md5

app=Flask(__name__)
app.secret_key="wadwadad"
bcrypt=Bcrypt(app)
mysql=MySQLConnector(app,'LoginRegister')
email_regex=re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/register', methods=["POST"])
def register():
    if len(request.form['first_name'])<2:
        flash('Your first name must be at least 2 characters')
        return redirect('/')
    elif len(request.form['last_name'])<2:
        flash('Your last name must be at least 2 characters')
        return redirect('/')
    elif not email_regex.match(request.form['email']):
        flash('Your email is invalid')
        return redirect('/')
    elif len(request.form['email'])<2:
        flash('You must input your email')
        return redirect('/')
    elif len(request.form['pw'])<8:
        flash('Your password must be at least 8 characters')
        return redirect('/')
    elif request.form['pw']!=request.form['pwc']:
        flash('Your password does not match the password confirmation')
        return redirect('/')
    else:
        session['action']="REGISTERED"
        pw=request.form['pw']
        pw_hash=bcrypt.generate_password_hash(pw)
        query="INSERT INTO users (email, first_name, last_name, pw_hash) VALUES (:email, :first_name, :last_name, :pw_hash)"
        data={
            'email':request.form['email'],
            'first_name':request.form["first_name"],
            'last_name':request.form["last_name"],
            'pw_hash':pw_hash
        }
        mysql.query_db(query, data)
        return render_template('success.html')

@app.route('/login', methods=["POST"])
def login():
    session['action']="LOGGED IN"
    pw=request.form['pw']
    query="SELECT * FROM users WHERE email=:email"
    data={
        'email':request.form['email']
    }
    user=mysql.query_db(query,data)
    if bcrypt.check_password_hash(user[0]['pw_hash'],pw):
        return render_template('success.html')
    else:
        flash('Your log in information did not match')
        return redirect('/')
app.run(debug=True)
