from flask_sqlalchemy import SQLAlchemy

# from datetime import datetime


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True )
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    post = db.relationship('Pokemon', backref = 'author', lazy = True)


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


    def save_user(self):
        db.session.add(self)
        db.session.commit()



class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False,)
    base_exp = db.Column(db.Integer, nullable=False,)
    ability = db.Column(db.String, nullable=False,)
    sprite_img = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    
    def __init__(self, name, base_exp, ability, sprite_img):
        self.name = name
        self.base_exp = base_exp
        self.ability = ability
        self.sprite_img = sprite_img

    def save_pokemon(self):
        db.session.add(self)
        db.session.commit()

    

