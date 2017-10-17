from flask import Flask, redirect, request, session, flash, render_template
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app=Flask(__name__)
app.secret_key="wallpassword"
bcrypt=Bcrypt(app)
mysql=MySQLConnector(app,'wall')
email_regex=re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template('index.html')

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
        query="INSERT INTO users (email, first_name, last_name, pw_hash, created_at, updated_at) VALUES (:email, :first_name, :last_name, :pw_hash, NOW(), NOW())"
        data={
            'email':request.form['email'],
            'first_name':request.form["first_name"],
            'last_name':request.form["last_name"],
            'pw_hash':pw_hash
        }
        mysql.query_db(query, data)
        flash('Your registration was successful')
        return redirect('/')

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
        session['id']=user[0]['id']
        flash('Welcome {}'.format(user[0]['first_name']))
        return redirect('/wall')
    else:
        flash('Your log in information did not match')
        return redirect('/')

@app.route('/message', methods=["POST"])
def post():
    message=request.form['message']
    print session['id']
    print message
    query="INSERT INTO messages (message,created_at,updated_at, users_id) VALUES (:message, NOW(), NOW(), :users_id)"
    data={
        'message':message,
        'users_id':session['id']
    }
    mysql.query_db(query,data)
    return redirect('/wall')

@app.route('/wall')
def wall():
    messages_query="SELECT messages.id,first_name,last_name,messages.created_at,message, users_id FROM messages\
                    JOIN users ON messages.users_id=users.id\
                    ORDER BY messages.created_at DESC"
    comments_query="SELECT comment, comments.id,first_name,last_name,message, messages_id FROM comments\
                    JOIN messages ON messages.id=comments.messages_id\
                    JOIN users ON users.id=comments.users_id\
                    ORDER BY comments.created_at"
    messages=mysql.query_db(messages_query)
    comments=mysql.query_db(comments_query)
    return render_template('wall.html', messages=messages, comments=comments)

@app.route('/comment/<id>', methods=["POST"])
def comment(id):
    query="INSERT INTO comments (comment, created_at, updated_at, users_id, messages_id) VALUES (:comment, NOW(), NOW(), :users_id, :messages_id)"
    data={
        'comment': request.form['comment'],
        'users_id': session['id'],
        'messages_id': id
    }
    mysql.query_db(query,data)
    return redirect('/wall')

@app.route('/delete/<message_id>', methods=["POST"])
def delete(message_id):
    delete_query= "DELETE FROM comments\
                    WHERE messages_id=:message_id"
    data={
        'message_id':message_id,
    }
    mysql.query_db(delete_query,data)
    delete_query= 'DELETE FROM messages\
                    WHERE id=:message_id'
    mysql.query_db(delete_query,data)
    return redirect('/wall')

@app.route('/logout',methods=["POST"])
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
