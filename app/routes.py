from flask import render_template, flash, redirect, url_for
from app import app, db
from .models import User
from app.forms import LoginForm, SignupForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Buddy')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.find_by_username(form.username.data)
        if user and user.check_password(form.password.data):
            flash('Login requested for user {}, remember_me={}'.format(
                form.username.data, form.remember_me.data))
            return redirect(url_for('index'))
        else:
            flash('Could not login')
            return redirect(url_for('login'))
    return render_template('login.html', title='Login', form=form) 

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        u = User(username=form.username.data)
        u.set_password(form.password.data)
        db.session.add(u)
        db.session.commit()
        flash('signup requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('signup.html', title='Sign up', form=form)