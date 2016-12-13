#-*- coding: utf-8 -*-

"""
Autores: Daniel Reyes, Ania Pietrzak, Alberto Miedes
Asignatura: Gestión de Información en la Web (GIW) - Práctica 7 - Grupo 1

Daniel Reyes, Ania Pietrzak y Alberto Miedes declaramos que esta solución es
fruto exclusivamente de nuestro trabajo personal. No hemos sido ayudados por
ninguna otra persona ni hemos obtenido la solución de fuentes externas, y
tampoco hemos compartido nuestra solución con nadie. Declaramos además que no
hemos realizado de manera deshonesta ninguna otra actividad que pueda mejorar
nuestros resultados ni perjudicar los resultados de los demás.
"""

from app.models.address import Address
from app.models.credit_card import CreditCard

class User:

    def __init__(self, options={}):

        self.id = options['_id']
        self.email = options['email'].encode('utf-8')
        self.webpage = options['webpage'].encode('utf-8')
        self.credit_card = options['credit_card']
        self.password = options['password'].encode('utf-8')
        self.name = options['name'].encode('utf-8')
        self.surname = options['surname'].encode('utf-8')
        self.address = options['address']

        self.likes = []
        for like in options['likes']:
            self.likes.append(like.encode('utf-8'))

        self.birthdate = options['birthdate']

    @staticmethod
    def valid_parameters():
        return {
                'id': True, '_id': True, 'email': True, 'webpage': True,
                'credit_card': True, 'password': True, 'name': True, 'surname': True,
                'address': True, 'birthdate':True
               }

    @staticmethod
    def build_from_db_record(record):
        new_user = User(record)
        new_user.credit_card = CreditCard({
            'expire_year': record['credit_card']['expire']['year'],
            'expire_month': record['credit_card']['expire']['month'],
            'number': record['credit_card']['number']
        })
        new_user.address = Address({
            'country': record['address']['country'],
            'zip': record['address']['zip'],
            'street': record['address']['street'],
            'num': record['address']['num'],
        })
        return new_user
