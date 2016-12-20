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


class CreditCard(EmbeddedDocument):
    propietario = StringField(required=True)

    # er: 16 digitos
    numero = StringField(regex='\d{16}$', required=True)

    # er: c/mes debe es de la forma "0X" o bien "1Y" con rango [01-12]
    mes_caducidad = StringField(regex='0[1-9]$|1[0-2]$', required=True)

    # er: años definidos desde 17 hasta 29
    anio_caducidad = StringField(regex='1[7-9]$|2[0-9]$', required=True)

    # er: 3 digitos
    cvv = StringField(max_length=3, regex='\d{3}$', required=True)
