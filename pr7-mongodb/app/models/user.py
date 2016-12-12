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
        self.address = options['address']

        self.likes = []
        for like in options['likes']:
            self.likes.append(like.encode('utf-8'))

        self.birthdate = options['birthdate']

    @staticmethod
    def valid_parameters():
        return {
                'id': True, '_id': True, 'email': True, 'webpage': True,
                'credit_card': True, 'password': True, 'name': True, 'surname': True,
                'address': True
               }
