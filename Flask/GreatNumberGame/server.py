from flask import Flask, request, redirect, render_template,session
import random
app=Flask(__name__)
app.secret_key="secret"
result=""
div=""
text=""
number=0
#<link rel="stylesheet" type="text/css" href="{{url_for('static',filename='style.css')}}">
@app.route('/')
def server():
    global number
    if number==0:
        number=random.randrange(1,101)
        session["number"]=number
    numberstr=str(session["number"])
    print session["number"]
    global result
    global div
    global text
    if result=="low":
        return render_template('index.html',guess="style=display:block;", text="Too low!",div="style='display:block;", again="style=display:none;")
    elif result=="high":
        return render_template('index.html',guess="style=display:block;", text="Too high!",div="style='display:block;", again="style=display:none;")
    elif result=="correct":
        text=numberstr+" was the number!"
        return render_template('index.html',guess="style=display:none;", div="style=display:none;",text=text, again="style=display:inline-block;")
    else:
        return render_template('index.html', guess="style=display:block;", div="style=display:none;", again="style=display:none;")

@app.route('/check',methods=['post'])
def check():
    global result
    global number
    if request.form['check']=="wrong":
        guess=int(request.form['guess'])
        if guess<session["number"]:
            result="low"
            return redirect('/')
        elif guess>session["number"]:
            result="high"
            return redirect('/')
        else:
            result="correct"
            return redirect('/')
    else:
        number=0
        result=""
        return redirect('/')


app.run(debug=True)
