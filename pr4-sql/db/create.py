#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

import seed

def create_books_table():

    # TODO: create books table

def create_customers_table():

    # TODO: create customers table

def create_purchases_table():

    # TODO: create purchases table

def db_create():

    # TODO: make connection to DB

    # TODO: drop database (if exists)

    create_books_table()
    create_customers_table()
    create_purchases_table()

    # TODO: close connection to DB

def db_setup():
    db_create()
    db_seed()
