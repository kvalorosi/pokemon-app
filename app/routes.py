from app import app
import requests
from urllib import response


from flask import render_template

from app.auth.forms import PokeForm


@app.route('/')
def land():
    return render_template('index.html')

@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon_data():
    form = PokeForm()
    response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    
    if response.ok:
           data = response.json()
           pokemon_name = data['name']
           ability = [ability['ability']['name'] for ability in data['abilities']]
           base_exp = data['base_experience']
           sprite_image = data['sprites']['front_shiny']

    else:
        return "Pokemon not found"

    
    # pokemon = Pokemon(name=pokemon_name, base_exp=base_exp, ability=ability, sprite_img=sprite_image)
    # pokemon.save_pokemon()
          
    
    

    return render_template('pokemon.html',form=form)


    


