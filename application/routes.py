# routes.py
from application import app
from flask import render_template

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register")
def register():
    return render_template('register.html')