#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

class CreditCard:

    def __init__(self, options={}):

        self.number = options['number']
        self.expire_year = options['expire_year']
        self.expire_month = options['expire_month']
