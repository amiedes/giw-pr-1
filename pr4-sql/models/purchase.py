#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

class Purchase:

    def __init__(self, options = {}):
        self.customer_id = options['customer_id']
        self.book_id = options['book_id']

    def save(self):
        
        # TODO: save object in BD
