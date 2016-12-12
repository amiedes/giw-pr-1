#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
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
