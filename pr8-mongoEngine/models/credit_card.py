#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

from mongoengine import EmbeddedDocument


class CreditCard(EmbeddedDocument):

    owner = StringField(required=True)

    # 16 digits long
    number = StringField(required=True, regex='^\d{16}$')

    # 2 digits long, range: [01-12]
    expiry_month = StringField(required=True, regex='^(0[1-9]|1[0-2])$')

    # 2 digits long
    expiry_year = StringField(required=True, regex='^\d{2}$')

    # 3 digits long
    cvv = StringField(required=True, regex='^\d{3}$')
