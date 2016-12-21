#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Autores: Daniel Reyes, Ania Pietrzak, Alberto Miedes
Asignatura: Gestión de Información en la Web (GIW) - Práctica 8 - Grupo 1

Daniel Reyes, Ania Pietrzak y Alberto Miedes declaramos que esta solución es
fruto exclusivamente de nuestro trabajo personal. No hemos sido ayudados por
ninguna otra persona ni hemos obtenido la solución de fuentes externas, y
tampoco hemos compartido nuestra solución con nadie. Declaramos además que no
hemos realizado de manera deshonesta ninguna otra actividad que pueda mejorar
nuestros resultados ni perjudicar los resultados de los demás.
"""

from mongoengine import connect
from models.credit_card import CreditCard
from models.order import Order
from models.product_line import ProductLine
from models.product import Product
from models.user import User

def insertar():

    alberto = User(
        dni = '76664938G',
        name = 'Alberto',
        first_surname = 'Miedes',
        birthdate = '1994-12-30'
    )
    alberto.save()

connect('giw_mongoengine')
insertar()
