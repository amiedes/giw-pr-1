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

class ProductLine(EmbeddedDocument):

    number_of_products = IntField(required=True, min_value=1, max_value=200)

    price_per_unit = DecimalField(required=True, precision=2)

    product_name = StringField(required=True)

    # Total price for this ProductLine
    total_price = DecimalField(required=True, precision=2)

    # Referencia al producto. Required.
    product = ReferenceField(Product)

    def clean(self):

        check_total_price()
        check_product_name()

    def check_total_price(self):

        calculated_total_price = self.number_of_products * self.price_per_unit

        if(self.total_price != calculated_total_price):
            raise ValidationError("ERROR: Precio de linea Mal Calculado")

    def check_product_name(self):

        if(self.product_name != self.product.name):
            raise ValidationError("ERROR: Nombre de Producto Erroneo")
