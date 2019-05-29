from flask import Flask, render_template, flash, redirect, url_for
from datetime import datetime
from app.forms import LoginForm, RegistrationForm
import re
from app import db 
from app import app


def get_date():
    date = datetime.now()
    return date

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/date")
def date():
    date = get_date()
    return render_template("date.html", date=date)

@app.route("/hello/<name>")
def hello_there(name):
    return render_template("hello_there.html", name=name,date=datetime.now())

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me ={}'.format(form.username.data, form.remember_me.data))
        return redirect("/api/data")
    return render_template('login.html', form=form)

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/api/data")
def get_data():
    return app.send_static_file("test_data.json")


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data, email=form.email.data)
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Congratulations, you are now a registered user!')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)