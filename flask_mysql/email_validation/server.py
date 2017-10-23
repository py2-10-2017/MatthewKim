from flask import Flask, redirect, render_template, request, flash, session
from mysqlconnection import MySQLConnector
import re
app=Flask(__name__)
app.secret_key="thisissescret!"
mysql=MySQLConnector(app,'email_validation')
email_regex=re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    query="SELECT * FROM emails"
    emails=mysql.query_db(query)
    return render_template('success.html', emails=emails, email=session['email'])

@app.route('/email_validation',methods=["POST"])
def check():
    email=request.form['email']
    session['email']=email
    if len(email)<1:
        flash('Email cannot be empty!')
        return redirect('/')
    elif not email_regex.match(email):
        flash('Email is not valid')
        return redirect('/')
    else:
        query ="INSERT INTO emails (email,date_created) VALUES (:email,NOW())"
        data = {
                'email':email
                }
        mysql.query_db(query,data)
        return redirect('/success')

@app.route('/<id>', methods=["POST"])
def getridof(id):
    query= "DELETE FROM emails WHERE id=:id"
    data={
        'id':id
    }
    flash('Successfully deleted Email!')
    mysql.query_db(query,data)
    return redirect ('/success')

@app.route('/return', methods=["POST"])
def doagain():
    return redirect('/')

app.run(debug=True)
