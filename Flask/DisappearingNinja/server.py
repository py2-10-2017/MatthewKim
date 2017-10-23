from flask import Flask, redirect, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def showall():
    ninja="leonardo"
    ninja2="michelangelo"
    ninja3="raphael"
    ninja4="donatello"
    return render_template('ninja.html', hidden="", ninja=ninja, ninja2=ninja2,ninja3=ninja3,ninja4=ninja4)

@app.route('/ninja/<color>')
def ninja(color):
    ninja2=""
    ninja3=""
    ninja4=""
    if color=="blue":
        ninja="leonardo"
    elif color=="orange":
        ninja="michelangelo"
    elif color=="red":
        ninja="raphael"
    elif color=="purple":
        ninja="donatello"
    else:
        ninja="notapril"
    return render_template("ninja.html", ninja=ninja, ninja2=ninja2,ninja3=ninja3,ninja4=ninja4, hidden="hidden")

app.run(debug=True)
