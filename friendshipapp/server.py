from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key="thiwdajdnoawjdn"
mysql = MySQLConnector(app,'friendsapp')
email_regex=re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)
@app.route('/friends', methods=['POST'])
def create():
    email=request.form['email']
    if len(email)<1:
        flash('Email cannot be empty!')
        return redirect('/')
    elif not email_regex.match(email):
        flash('Email is not valid')
        return redirect('/')
    else:
        query = "INSERT INTO friends (first_name, last_name, email, dated_created, date_updated) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
        # We'll then create a dictionary of data from the POST data received.
        data = {
                 'first_name': request.form['first_name'],
                 'last_name': request.form['last_name'],
                 'email': email
               }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        return redirect('/')
@app.route('/<id>', methods=["POST"])
def button(id):
    query="SELECT * FROM friends WHERE id=:id"
    data={
        'id':id
        }
    friend=mysql.query_db(query,data)
    print friend[0]['first_name']
    if request.form['button']=="Edit":
        return render_template('edit.html',id=friend[0]['id'], first_name=friend[0]['first_name'], last_name=friend[0]['last_name'], email=friend[0]['email'])
    else:
        idstr=str(friend[0]['id'])
        return redirect('/friends/delete/'+idstr)


@app.route('/friends/delete/<id>')
def delete(id):
    query="DELETE FROM friends WHERE id=:id"
    data={
    'id':id
    }
    flash('Successfully deleted Email!')
    mysql.query_db(query,data)
    return redirect('/')

@app.route('/edit/<id>', methods=["POST"])
def edit(id):
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    email=request.form['email']
    query="UPDATE friends SET first_name=:first_name, last_name=:last_name, email=:email, date_updated=NOW() WHERE id=:id"
    data={
        'id':id,
        'first_name':first_name,
        'last_name':last_name,
        'email':email
    }
    mysql.query_db(query,data)
    return redirect('/')


app.run(debug=True)
