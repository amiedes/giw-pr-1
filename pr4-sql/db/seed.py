#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

def seed_books_table():
    print "seed_customers_table()"
    # TODO: parse db/seeds/libros.csv and insert its records into DB


def seed_customers_table():
    print "seed_customers_table()"
    # TODO: parse db/seeds/compradores.csv and insert its records into DB

def seed_purchases_table():
    print "seed_customers_table()"
    # TODO: parse db/seeds/compras.csv and insert its records into DB

def db_seed():
    # TODO: make connection to DB

    seed_books_table()
    seed_customers_table()
    seed_purchases_table()

    # TODO: close connection to DB
