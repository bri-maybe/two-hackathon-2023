import os
from src import main

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = r"-sadfji3_dsfjjn"

@app.route("/")
def root():
    return render_template("home.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/create/', methods=('GET', 'POST'))
def create():
    print(request.form)
    if request.method == 'POST':
        name = request.form['name']
        if not name:
            flash('name is required!')
        elif main.user_exists(name):
            flash('name has already been taken!')
        else:
            main.make_new_user(request.form)
            return redirect(url_for('use', name=name))

    return render_template('create.html')

@app.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        name = request.form['name']
        if not name:
            flash('Name is required!')
        elif main.user_exists(name):
            return redirect(url_for('use', name=name))
        else:
            flash('Name does not exist.')

    return render_template("login.html")

@app.route("/use")
def use():
    if not "name" in request.args:
        return "bad request, missing name"

    name = request.args['name']

    return render_template("use.html",name = name)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port = 8080, debug=True)
