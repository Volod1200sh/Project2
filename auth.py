from flask import Blueprint, render_template, redirect, url_for, request
from pip._internal.network import auth
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
...
@auth.route('/signup', methods=['POST'])
def signup_post(database=None):
    email = request.form.get('email')
    login = request.form.get('login')
    name = request.form.get('name')
    surname = request.form.get('surname')
    year = request.form.get('year')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() in database

    if user:
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))