# -*- coding: utf-8 -*-

import requests

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

payload = {
    'nickname': 'apietrzak',
    'name': 'Ania Pietrzak',
    'country': 'Polonia',
    'email': 'apietrzak@mail.dev',
    'password': '1234',
    'password2': '1234'
}

response = requests.post('http://localhost:8080/signup', data=payload)

print(response.text)

payload = {
    'nickname': 'dreyes',
    'name': 'Daniel Reyes',
    'country': 'España',
    'email': 'dreyes@mail.dev',
    'password': '1234',
    'password2': '1234'
}

response = requests.post('http://localhost:8080/signup', data=payload)

print(response.text)
