#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

class User:

    def __init__(self, options={}):

        self.id = options['_id']
        self.email = options['email'].encode('utf-8')
        self.webpage = options['webpage'].encode('utf-8')
        self.credit_card = options['credit_card']
        self.password = options['password'].encode('utf-8')
        self.name = options['name'].encode('utf-8')
        self.surname = options['surname'].encode('utf-8')
        self.address = options['address'].encode('utf-8')
        self.likes = options['likes']
        self.birthdate = options['birthdate']
