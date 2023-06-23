from urllib import response
from flask import Blueprint, flash, render_template, request, redirect, session, url_for
from flask_login import current_user
import requests
from .forms import RegisterForm
from ..models import User 
from ..models import Pokemon
from .forms import LoginForm
from .forms import PokeForm
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
        return redirect(url_for('auth.pokemon_data'))


            
    return render_template('login.html',form=form)


@auth.route('/pokemon', methods=['GET', 'POST'])
def pokemon_data():
    form = PokeForm()
    if request.method == 'POST':
        if form.validate():
            name = form.poke_name.data
            pokemon = Pokemon.query.all()
            # catch = pokemon.caught.count()
            # pokemon.catch = catch

            # if pokemon:
            #     print(pokemon.name)
            # else:
            #     print("pokemon doesn't exist")
                
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
            if response.ok:
                data = response.json()
                global information 
                pokemon = {}
                pokemon['name'] = data['forms'][0]['name'] 
                pokemon['ability'] = data['abilities'][0]['ability']['name']
                pokemon['base_exp'] = data['base_experience']
                pokemon['sprite'] = data['sprites']['front_shiny']
                pokemon['attack'] = data['stats'][1]['base_stat']
                pokemon['defense'] = data['stats'][2]['base_stat']
                pokemon['hp'] = data['stats'][0]['base_stat']
                information = pokemon

                
                new_pokemon=Pokemon(name=pokemon['name'],
                                        base_exp=pokemon['base_exp'],
                                        ability=pokemon['ability'],
                                        sprite=pokemon['sprite'])
                new_pokemon.save_pokemon()
 
                
                return redirect(url_for('auth.info'))
            else:
                return "Pokemon not found"
            
                
    return render_template('pokemon.html',form=form)



@auth.route('/info')
def info():
    
    return render_template('info.html', pokemon=information)

@auth.route('/card', methods= ['GET', 'POST'])
def create_card():
    form = CreateCardForm()

    return render_template('info.html', form=form)



@auth.route('/pokemon/catch/<int:pokemon_id>')
def my_poke(pokemon_id):
    pokemon = Pokemon.query.get(pokemon_id)
    pokes = current_user.caught
    print(pokes)
    if pokemon in pokes:
        flash(f"You've already caught this Pokemon!", 'warning')

    else:
        pokemon.caught_poke(current_user)
        
        # db.session.commit()
        flash(f"Pokemon added to your team!", 'success')
        return redirect(url_for('auth.info'))





    


