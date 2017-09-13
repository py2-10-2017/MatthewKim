from flask import Flask,redirect,session,request, render_template
app=Flask(__name__)
app.secret_key="secret"

@app.route('/')
def index():
    session['count']+=1
    return render_template('index.html')

@app.route('/+2counter', methods=["post"])
def plus2():
    session['count']+=1
    return redirect('/')

@app.route('/reset', methods=["post"])
def reset():
    session['count']=0
    return redirect('/')
    
app.run(debug=True)
