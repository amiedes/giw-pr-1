# -*- coding: utf-8 -*-

import requests

from pymongo import MongoClient

# Drop user collection
client = MongoClient()
db = client.giw
db.user.delete_many({})
client.close()

# Create new amiedes user

payload = {
    'nickname': 'amiedes',
    'name': 'Alberto Miedes Garcés',
    'country': 'España',
    'email': 'amiedes@mail.dev',
    'password': '1234',
    'password2': '1234'
}

response = requests.post('http://localhost:8080/signup', data=payload)
print(response.text)

# Successful login

payload = {
    'nickname': 'amiedes',
    'password': '1234'
}

response = requests.post('http://localhost:8080/login', data=payload)
print(response.text)

# Failing login

payload = {
    'nickname': 'amiedes',
    'password': 'wrong_password'
}

response = requests.post('http://localhost:8080/login', data=payload)
print(response.text)
