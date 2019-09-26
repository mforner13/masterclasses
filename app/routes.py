from flask import render_template, url_for, flash, redirect, request
from flask_login import current_user, login_user, login_required, logout_user
from app.models import *
from app import app


@app.route('/')
@app.route('/index')
@login_required
def index():
    masterclasses = Masterclass.query.order_by(Masterclass.timestamp.asc()).all()
    return render_template('index.html', title='Home', user=User, masterclasses=masterclasses)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email-address']).first()
        if user is None or not user.check_password(request.form['password']):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user,
                # remember=request.form.remember_me.data
                   )
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

