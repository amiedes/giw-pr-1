#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

class User:

    def __init__(self, options={}):

        self.id = options['_id']
        self.email = options['email']
        self.name = options['name']
        self.surname = options['surname']
        self.webpage = options['webpage']
        self.birthdate = options['birthdate']
