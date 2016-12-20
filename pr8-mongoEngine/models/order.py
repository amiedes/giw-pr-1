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

    # TODO: pending to refactor this method
    def clean(self):
        total = float(self.total_price)
        total_from_lines = 0.00
        i = 0
        for i in range(len(self.lineas_pedido)):
            total_linea = float(self.lineas_pedido[i].precio_total)
            total_from_lines = total_from_lines + total_linea

        if(total != total_from_lines):
            raise ValidationError("ERROR: No concuerdan los totales")
