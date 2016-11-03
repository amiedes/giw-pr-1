#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

class Libro:

    def __init__(self, options = {}):
        self.title = options['title']
        self.author = options['author']
        self.editorial = options['editorial']
        self.format = options['format']
        self.entry_date = options['entry_date']
        self.country = options['country']
        self.price = options['price']
        self.annotations = options['annotations']

    def save(self):

        # TODO: save object in BD
