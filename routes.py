from app import app, db
from models import User, Book, Review, Author
from flask import render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


#class form(FlaskForm):
#    name = StringField("What's your name?")
#    submit = SubmitField("Submit")
#   

 
@app.route('/')
def index():
    return render_template('hello.html')