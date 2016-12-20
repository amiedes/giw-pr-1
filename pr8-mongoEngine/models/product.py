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


class Product(Document):
    # er: numero de 13 digitos
    codigo = StringField(primary_key=True, regex='\d{13}$')

    nombre = StringField(required=True)

    # er: combinacion de digitos --> Natural
    categoria = StringField(required=True, regex='\d*$')

    # er: combinacion de digitos --> Natural
    subcategoria = ListField(StringField(), regex='\d*$')

    def clean(self):
        # comprobar si tiene lista de categorias secundarias
        if len(self.subcategoria) > 0:
            # anadir categoria como primer elemento de subcategoria si todavia
            # no aparace
            if self.subcategoria[0] != self.categoria:
                self.subcategoria.append(0, self.categoria)
