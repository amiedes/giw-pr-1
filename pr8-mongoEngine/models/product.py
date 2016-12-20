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

class Product(Document):

    # 13 digits, TODO: Format: EAN-13
    barcode = StringField(primary_key=True, regex='^\d{13}$')

    name = StringField(required=True)

    # Categoría principal
    category = IntField(required=True, min_value=1)

    # List of secondary categories
    subcategories = ListField(IntField(min_value=1))

    def clean(self):
        # TODO: esto está mal, mirar como se comprueba que esté presente
        # comprobar si tiene lista de categorias secundarias
        if len(self.subcategories.size) > 0:
            # anadir categoria como primer elemento de subcategoria si todavia
            # no aparace
            if self.subcategories[0] != self.category:
                self.subcategories.append(0, self.category)
