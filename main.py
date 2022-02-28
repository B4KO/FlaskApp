from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

S
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =
app.config['SECRET_KEY'] = "Sorry i'm not your mom, Putin"


db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    release = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return "This is {0}".format(self.name)

class form(FlaskForm):
    name = StringField("What's your name?")
    submit = SubmitField("Submit")
    
@app.route('/')
@app.route('')
def index():
    