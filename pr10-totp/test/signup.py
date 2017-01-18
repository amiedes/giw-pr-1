# -*- coding: utf-8 -*-

"""
Autores: Daniel Reyes, Ania Pietrzak, Alberto Miedes
Asignatura: Gestión de Información en la Web (GIW) - Práctica 10 - Grupo 1

Daniel Reyes, Ania Pietrzak y Alberto Miedes declaramos que esta solución es
fruto exclusivamente de nuestro trabajo personal. No hemos sido ayudados por
ninguna otra persona ni hemos obtenido la solución de fuentes externas, y
tampoco hemos compartido nuestra solución con nadie. Declaramos además que no
hemos realizado de manera deshonesta ninguna otra actividad que pueda mejorar
nuestros resultados ni perjudicar los resultados de los demás.
"""

import requests
from pymongo import MongoClient

# Drop user collection
client = MongoClient()
db = client.giw
db.users.delete_many({})
client.close()

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
