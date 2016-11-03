#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

class Comprador:

    def __init__(self, options = {}):
        self.name = options['name']
        self.birthdate = options['birthdate']
        self.telephone = options['telephone']
        self.address = options['address']
        self.town = options['town']
        self.annotations = options['annotations']

    def save(self):

        # TODO: save object in BD
