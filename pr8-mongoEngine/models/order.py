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

class Order(Document):

    total_price = DecimalField(required=True, precision=2)

    date = ComplexDateTimeField(required=True)

    # Product line lists
    product_lines = ListField(
        EmbeddedDocumentField(Linea_Pedido, required=True),
        required=True
    )

    def clean(self):
        check_total_price()

    def check_total_price(self):
        total_price = float(self.total_price)
        calculated_total_price = 0.00

        for product_line in self.product_lines:
            calculated_total_price += product_line.total_price

        if(total_price != calculated_total_price):
            raise ValidationError("Order total_price is not correctly calculated")
