from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL') or 'sqlite:///myDB.db'
app.config['SECRET_KEY'] = "Sorry i'm not your mom, Putin"


db = SQLAlchemy(app)

import models

import routes 

