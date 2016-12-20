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


from mongoengine import *

class User(Document):

    # 1 digit or letter (X,Y,Z) + 7 digits + 1 letter
    dni = StringField(primary_key=True, regex='^(\d|[X-Z]|[x-z])\d{7}([A-Z]|[a-z])$')

    name = StringField(required=True)

    first_surname = StringField(required=True)

    second_surname = StringField()

    # Format: 'AAAA-MM-DD', truncate 'time' later
    birthdate = DateTimeField(required=True)

    # Last 10 access to system
    last_accesses = ListField(ComplexDateTimeField())

    # Credit card list
    credit_cards = ListField(EmbeddedDocumentField(CreditCard))

    # References to orders list
    orders = ListField(ReferenceField(Order, reverse_delete_rule=PULL))

    def verify_dni_nie(self):
        letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B',
                  'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
        dni = self.dni.upper()
        id_number = 0
        offset = 0
        last_letter = dni[len(dni) - 1]
        # calcular offset en caso de NIE
        if(dni[0].isalpha() and dni[0] != 'X'):
            offset = offset + 10000000
            if(dni[0] == 'Z'):
                offset = offset + 10000000
        else:
            offset = 0

        # obtener la cifra para calcular el digito de control
        dni = ''
        i = 0
        for i in range(len(self.dni)):
            if(self.dni[i].isalpha()):
                continue
            else:
                dni = dni + self.dni[i]
        id_number = int(dni)
        id_number = id_number + offset

        # calculo y comprobacion
        correct_index = id_number % 23
        correct_letter = letras[correct_index]
        if(correct_letter != last_letter):
            raise ValidationError("El DNI o NIE introducido No Existe")
