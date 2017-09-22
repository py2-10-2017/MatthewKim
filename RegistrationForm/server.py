from flask import Flask, request, redirect, session, flash, render_template
app=Flask(__name__)
app.secret_key="thisiskey"
import re, datetime, time
email_regex=re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check',methods=['post'])
def check():
    email=request.form['email']
    firstname=request.form['first_name']
    lastname=request.form['last_name']
    password=request.form['password']
    passwordc=request.form['confirm_password']
    date=request.form['date']
    if len(email)<1:
        flash('You must put your email')
        return redirect('/')
    elif not email_regex.match(email):
        flash('Inavalid Email provided')
        return redirect('/')
    elif len(firstname)<1:
        flash('You must put your firstname')
        return redirect('/')
    elif firstname.isalpha()==False or lastname.isalpha()==False:
        flash('Your first and last name must consist of only alphabetic characters')
        return redirect('/')
    elif len(lastname)<1:
        flash('You must put your last name')
        return redirect('/')
    elif len(date)<1:
        flash('You must provide your date of birth')
        return redirect('/')
    elif len(password)<1:
        flash('You must provide a password')
        return redirect('/')
    elif len(password)<8:
        flash('Your password must be at least 8 characters')
        return redirect('/')
    elif re.search('[0-9]',password) is None:
        flash('Make sure your password contains at least one number')
        return redirect('.')
    elif re.search('[A-Z]',password) is None:
        flash('Make sure your password contains at least one capitalized letter')
        return redirect('/')
    elif len(passwordc)<1:
        flash('You must confirm your password')
        return redirect('/')
    elif passwordc!=password:
        flash('Your password does not match the confirmation')
        return redirect('/')
    else:
        flash('You have successfully submitted your information!!')
        return redirect('/')

app.run(debug=True)
