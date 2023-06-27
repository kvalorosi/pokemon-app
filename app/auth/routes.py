from urllib import response
from flask import Blueprint, flash, render_template, request, redirect, session, url_for
from flask_login import current_user
import requests
from .forms import RegisterForm
from ..models import User 
from .forms import LoginForm
import json
from .forms import CreateCardForm
from flask_login import login_user, logout_user

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            print(username,email,password)

            user = User(username, email, password)
            user.save_user()
            return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            password = form.password.data
        return redirect(url_for('pokemon_data'))


    return render_template('login.html',form=form)






