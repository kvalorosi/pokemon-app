from app import app
import requests
from urllib import response


from flask import render_template

from app.auth.forms import PokeForm


@app.route('/')
def land():
    return render_template('index.html')


    
   
    


