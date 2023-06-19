from urllib import response
from flask import Blueprint, render_template, request, redirect, url_for
import requests
from .forms import RegisterForm
from ..models import User 
from ..models import Pokemon
from .forms import LoginForm
from .forms import PokeForm
import json




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
            # return redirect(url_for('auth.poke_info'))


            # user = User(username, password)
    return render_template('login.html',form=form)


# @auth.route('/pokemon', methods=['GET', 'POST'])
# def pokemon_data():
#     form = PokeForm()
#     response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    
#     if response.ok:
#            data = response.json()
#            pokemon_name = data['name']
#            ability = [ability['ability']['name'] for ability in data['abilities']]
#            base_exp = data['base_experience']
#            sprite_image = data['sprites']['front_shiny']

#     else:
#         return "Pokemon not found"

    
#     # pokemon = Pokemon(name=pokemon_name, base_exp=base_exp, ability=ability, sprite_img=sprite_image)
#     # pokemon.save_pokemon()
          
    
    

#     return render_template('pokemon.html',form=form)

