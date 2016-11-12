#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

import sqlite3


def db_open_connection():

    print "Opening connection to db..."

    # connect to the database and get a cursor object
    con = sqlite3.connect('practica6')
    cur = con.cursor()

    return {'connection': con, 'cursor': cur}


def db_close_connection(db):

    # commit changes and close connection
    db['connection'].commit()
    db['cursor'].close()
    db['connection'].close()


def create_consulates_table(cursor):

    print "Creating consulates table..."

    cursor.execute(
        "CREATE TABLE consulates ( \
            id              INT(16)         NOT NULL PRIMARY KEY UNIQUE, \
            name            VARCHAR(128)    NOT NULL UNIQUE,\
            postal_code     INT(16)         DEFAULT NULL,\
            neighborhood    VARCHAR(32)     DEFAULT NULL,\
            district        VARCHAR(32)     DEFAULT NULL,\
            latitude        DECIMAL(8,2)    DEFAULT NULL,\
            longitude       DECIMAL(8,2)    DEFAULT NULL \
        )"
    )


def drop_consulates_table(cursor):

    cursor.execute("DROP TABLE IF EXISTS consulates")

    print "Table consulates dropped"


def db_create():

    db = db_open_connection
    create_consulates_table(db['cursor'])
    db_close_connection(db)


def db_reset():

    print "Reseting database..."

    db = db_open_connection()
    drop_consulates_table(db['cursor'])
    create_consulates_table(db['cursor'])
    db_close_connection(db)
