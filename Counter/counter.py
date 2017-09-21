from flask import Flask,redirect,session,request, render_template
app=Flask(__name__)
app.secret_key="secret"
counter=0

@app.route('/')
def index():
    global counter
    counter+=1
    session['count']=counter
    return render_template('index.html')

@app.route('/+2counter', methods=["post"])
def plus2():
    global counter
    counter+=1
    return redirect('/')

@app.route('/reset', methods=["post"])
def reset():
    global counter
    counter=0
    return redirect('/')

app.run(debug=True)
