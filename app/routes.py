from app import app
import requests
from urllib import response


from flask import render_template
from .models import User




@app.route('/')
def land():
    user_list = User.query.all()
    print(user_list)
    return render_template('index.html')


    
   
    


