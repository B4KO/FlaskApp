import requests
import random
from datetime import datetime, timedelta

def gen_datetime(min_year=1900, max_year=datetime.now().year):
    
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()

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
    
    