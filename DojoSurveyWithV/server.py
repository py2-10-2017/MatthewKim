from flask import Flask, redirect, request, render_template, flash, session
app=Flask(__name__)
app.secret_key="secret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=["POST"])
def create_user():
    name=request.form['name']
    location=request.form['location']
    language=request.form['language']
    comment=request.form['comment']
    if len(name)<1:
        flash("You need to put yo name")
        return render_template('index.html')
    elif len(comment)<1:
        flash("You need to put yo name")
        return render_template('index.html')
    elif len(comment)>120:
        flash("Your comment cannot be longer than 120 Characters")
        return render_template('index.html')
    else:
        return render_template('result.html', name=name, location=location, language=language, comment=comment)


app.run(debug=True)
