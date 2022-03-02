import requests
import random
from app import db
from models import User, Author, Book, Review
from functions import gen_datetime

r = requests.get('https://jsonplaceholder.typicode.com/users')

users = r.json()

for user in users:
    print("User \n")
    print("______\n")
    print("ID: "+str(user['id']))
    print("\n")
    
    print("NAME: "+str(user['name']))
    print("\n")
    
    print("EMAIL: "+str(user['email']))
    print("\n")
    
    print("BIRTHDATE: "+str(gen_datetime()))
    print("\n") 
    
    userDb = User(name = str(user['name']), email = str(user['email']), birthdate = str(gen_datetime), date_added= str(datetime.utcnow))
    db.session.add(userDb)
    
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
    
    