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


class ProductLine(EmbeddedDocument):
    # er: combinacion de digitos --> Natural
    cantidad_productos = StringField(required=True, regex='\d*$')

    # er: float con dos cifras decimales
    precio_unidad = StringField(required=True, regex='\d*\.\d{2}$')
    nombre_producto = StringField(required=True)

    # er: float con dos cifras decimales
    precio_total = StringField(required=True, regex='\d*\.\d{2}$')
    producto = ReferenceField(Producto)

    def clean(self):
        # comprobar nombre de producto
        nombre = self.nombre_producto
        nombre_real = self.producto.nombre
        if(nombre_real != nombre):
            raise ValidationError("ERROR: Nombre de Producto Erroneo")

        # comprobar precio total de linea
        total = float(self.precio_total)
        cantidad = int(self.cantidad_productos)
        precio_unidad = float(self.precio_unidad)
        total_calculado = cantidad * precio_unidad
        if(total != total_calculado):
            raise ValidationError("ERROR: Precio de linea Mal Calculado")
