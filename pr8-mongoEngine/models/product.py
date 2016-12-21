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

from mongoengine import *

class Product(Document):

    # 13 digits
    barcode = StringField(primary_key=True, regex='^\d{13}$')

    name = StringField(required=True)

    # Categoría principal
    category = IntField(required=True, min_value=1)

    # List of secondary categories
    subcategories = ListField(IntField(min_value=1))

    def clean(self):

        check_subcategories()
        check_barcode_checksum()

    def check_subcategories(self):

        if (self.subcategories != None) and len(self.subcategories) > 0:
            # add category as first element if yet not in subcategories
            if self.subcategories.first != self.category:
                self.subcategories.append(0, self.category)

    def check_barcode_checksum(self):

        calculated_checksum = 0
        for idx, digit in enumerate(barcode):
            if idx == 12:
                checksum_digit = int(digit)
            elif idx % 2 == 0:
                calculated_checksum += 3 * int(digit)
            else:
                calculated_checksum += 1 * int(digit)

        if calculated_checksum != checksum_digit:
            raise ValidationError("Error in checksum")
