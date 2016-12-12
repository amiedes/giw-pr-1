#-*- coding: utf-8 -*-

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

class Address:

    def __init__(self, options={}):

        self.country = options['country'].encode('utf-8')
        self.zip = int(options['zip'])
        self.street = options['street'].encode('utf-8')
        self.num = int(options['num'])

    def pretty(self):
        formatted_address = "C/ " + self.street + " Nº " + str(self.num) + ", " + self.country + " " + str(self.zip)
        return formatted_address
