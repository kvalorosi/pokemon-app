
from flask import Blueprint, flash, render_template, request, redirect, session, url_for
from flask_login import current_user, login_user, logout_user
from .forms import RegisterForm, LoginForm
from ..models import User 

from werkzeug.security import check_password_hash



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

            user = User.query.filter_by(username=username).first()
            if user:
                print(user.password)
                # if check_password_hash(user.password, password):  SINCE WE HAVEN'T IMPLEMENTED THIS YET IT WAS PREVENTING LOGIN!
                if user.password == password: #BASIC VERSION WORKS
                    flash("You've logged in", 'success')
                    login_user(user)
                    return redirect(url_for('pokemon_data'))
                else:
                    flash('Wrong pass, try again', 'warning')
                    
            else:
                flash('cannot find that user. . . ', 'danger')
    
    return render_template('login.html',form=form)

@auth.route('/logout')
def logout():
    flash("you're logged out, See YA!", 'secondary')
    logout_user()
    return redirect(url_for('land'))







