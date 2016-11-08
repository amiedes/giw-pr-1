#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

from seed import db_seed
import sqlite3


def create_books_table(cur):

    print "CREANDO TABLA Libros EN BASE DE DATOS"
    cur.execute("DROP TABLE IF EXISTS Libros")
    cur.execute(
        "CREATE TABLE Libros ( \
            registro        INT(4)          NOT NULL    PRIMARY KEY UNIQUE,\
            titulo          VARCHAR(35)     NOT NULL    DEFAULT ' ' UNIQUE,\
            escritor        VARCHAR(35)     NOT NULL    DEFAULT ' ',\
            editorial       VARCHAR(20)     NOT NULL    DEFAULT ' ',\
            soporte         VARCHAR(35)     NOT NULL    DEFAULT 'LIBRO',\
            fecha_entrada   DATE            NOT NULL    DEFAULT NULL,\
            pais            VARCHAR(20)     NOT NULL    DEFAULT '0000-00-00',\
            importe         DECIMAL(8,2)    NOT NULL    DEFAULT 0.0,\
            anotaciones     BLOB\
        )"
    )


def create_customers_table(cur):

    print "CREANDO TABLA Compradores EN BASE DE DATOS"
    cur.execute("DROP TABLE IF EXISTS Compradores")
    cur.execute(
        "CREATE TABLE Compradores (\
            registro    INT(4)      NOT NULL    PRIMARY KEY             UNIQUE,\
            nombre      VARCHAR(35) NOT NULL    DEFAULT ' '             UNIQUE,\
            fecha_nacim DATE        NOT NULL    DEFAULT '0000-00-00',\
            telefono    VARCHAR(10)             DEFAULT NULL,\
            domicilio   VARCHAR(35)             DEFAULT NULL,\
            poblacion   VARCHAR(25)             DEFAULT NULL,\
            anotaciones TEXT\
        )"
    )


def create_purchases_table(cur):

    print "CREANDO TABLA Compras EN BASE DE DATOS"
    cur.execute("DROP TABLE IF EXISTS Compras")
    cur.execute(
        "CREATE TABLE Compras (\
            registro        INT(4)  NOT NULL    PRIMARY KEY UNIQUE,\
            id_comprador    INT(4)  NOT NULL    DEFAULT ' ',\
            id_libro        INT(4)  NOT NULL    DEFAULT ' '\
        )"
    )


def db_create():

    # connect to the database and get a cursor object
    conn = sqlite3.connect('Libreria')
    cur = conn.cursor()

    # create all db tables
    create_books_table(cur)
    create_customers_table(cur)
    create_purchases_table(cur)

    # commit changes and close connection
    conn.commit()
    cur.close()
    conn.close()


def db_setup():
    db_create()
    db_seed()
