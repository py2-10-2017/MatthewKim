from flask import Flask, request, redirect, render_template, session
app=Flask(__name__)
import random, datetime
app.secret_key='thisisthekey'
step=0
text=""

@app.route('/')
def server():
    global step
    global text
    if step==0:
        session['gold']=step
    return render_template('index.html',money=session['gold'], activity=text)


@app.route('/process_money',methods=["post"])
def money():
    global text
    global step
    time=str(datetime.datetime.now())
    if 'activity' not in session:
        session['activity']=[]
    activity=session['activity']
    if request.form['type']=="farm":
        earn=random.randrange(10,21)
        session['gold']+=earn
        step+=1
        earnstr=str(earn)
        activity.append("Earned "+earnstr+" gold from the farm! ("+time+")")
        return redirect ('/')
    elif request.form['type']=="cave":
        earn=random.randrange(5,11)
        session['gold']+=earn
        step+=1
        earnstr=str(earn)
        activity.append("Earned "+earnstr+" gold from the cave! ("+time+")")
        return redirect ('/')
    elif request.form['type']=="house":
        earn=random.randrange(2,6)
        session['gold']+=earn
        step+=1
        earnstr=str(earn)
        activity.append("Earned "+earnstr+" gold from the house! ("+time+")")
        return redirect ('/')
    elif request.form['type']=="casino":
        earn=random.randrange(-50,51)
        session['gold']+=earn
        step+=1
        earnstr=str(earn)
        if earn>=0:
            activity.append("Earned "+earnstr+" gold from the casino! ("+time+")")
        elif earn<0:
            earn*=-1
            earnstr=str(earn)
            activity.append("Lost "+earnstr+" gold from the casino...Ouch...Is gambling worth it?? ("+time+")")
        return redirect ('/')
    elif request.form['type']=='Reset':
        step=0
        session.pop('activity')
        return redirect ('/')
    session['activity']=activity
app.run(debug=True)
