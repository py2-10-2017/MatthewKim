from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, "mydb")

@app.route('/')
def index():
    query = mysql.query_db("SELECT * FROM users")
    return "{}".format(query)

app.run(debug=True)
