from flask_login import current_user
from app import app
import requests
from urllib import response


from flask import flash, redirect, render_template, request, url_for

from app.auth.forms import CreateCardForm, PokeForm
from .models import Pokemon, User




@app.route('/')
def land():
    user_list = User.query.all()
    print(user_list)
    return render_template('base.html')

@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon_data():
    form = PokeForm()
    if request.method == 'POST':
        if form.validate():
            name = form.poke_name.data
            pokemon = Pokemon.query.filter_by(name=name).first()
            if pokemon:
                print(pokemon)
                return render_template('pokemon.html', form=form, poke=pokemon)
            
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
            if response.ok:
                data = response.json()
                print(data)
                pokemon = {}
                pokemon['name'] = data['forms'][0]['name'] 
                pokemon['ability'] = data['abilities'][0]['ability']['name']
                pokemon['base_exp'] = data['base_experience']
                pokemon['sprite'] = data['sprites']['front_shiny']
                pokemon['attack'] = data['stats'][1]['base_stat']
                pokemon['defense'] = data['stats'][2]['base_stat']
                pokemon['hp'] = data['stats'][0]['base_stat']
                
                new_pokemon = Pokemon(
                    name=pokemon['name'],
                    base_exp=pokemon['base_exp'],
                    ability=pokemon['ability'],
                    sprite=pokemon['sprite'])
                
                new_pokemon.save_pokemon()
                return render_template('pokemon.html', form=form, poke=new_pokemon)
            else:
                flash('Pokemon not found plz try again!', 'danger')
                return redirect(url_for('pokemon_data'))
                
                
    return render_template('pokemon.html',form=form)

@app.route('/card', methods= ['GET', 'POST'])
def create_card():
    form = CreateCardForm()

    return render_template('pokemon', form=form)

@app.route('/info/catch/<int:pokemon_id>', methods=['GET', 'POST'])
def my_poke(pokemon_id):
    pokemon = Pokemon.query.get(pokemon_id)
    pokes = current_user.caught
    print(pokes)
    if pokemon in pokes:
        flash(f"You've already caught this Pokemon!", 'warning')
        #This isn't done, where should this go? I typed in pokemon...and pokemon_data neither are working. 
        return redirect(url_for('pokemon'))

    else:
        pokemon.caught_poke(current_user)
        
        # db.session.commit()
        flash(f"Pokemon added to your team!", 'success')
        #This isn't done, where should this go?
        return redirect(url_for('pokemon'))




    
   
    


