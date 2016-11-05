#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""
from seed import db_seed
import sqlite3

def create_books_table(cur):
    
    print "CREANDO TABLA Libros EN BASE DE DATOS"
    cur.execute("DROP TABLE IF EXISTS Libros")
    cur.execute("CREATE TABLE Libros (registro INTEGER NOT NULL PRIMARY KEY UNIQUE, " +
                                           "titulo TEXT NOT NULL DEFAULT ' ' UNIQUE, " +
                                           "escritor TEXT NOT NULL DEFAULT ' ', " +
                                           "editorial TEXT NOT NULL DEFAULT ' ', " +
                                           "soporte TEXT NOT NULL DEFAULT 'LIBRO', " +
                                           "fecha_entrada TEXT NOT NULL DEFAULT NULL, " +
                                           "pais TEXT NOT NULL DEFAULT '0000-00-00', " +
                                           "importe NUMERIC NOT NULL DEFAULT '0.0', " +
                                           "anotaciones BLOB)")                                    
                                                                                       
def create_customers_table(cur):

    print "CREANDO TABLA Compradores EN BASE DE DATOS"
    cur.execute("DROP TABLE IF EXISTS Compradores")
    cur.execute("CREATE TABLE Compradores (registro INTEGER NOT NULL PRIMARY KEY UNIQUE, " +
                                           "nombre TEXT NOT NULL DEFAULT ' ' UNIQUE, " +
                                           "fecha_nacim TEXT NOT NULL DEFAULT '0000-00-00', " +
                                           "telefono TEXT DEFAULT NULL, " +
                                           "domicilio TEXT DEFAULT NULL, " +
                                           "poblacion TEXT DEFAULT NULL, " +
                                           "anotaciones TEXT)")
def create_purchases_table(cur):
    
    print "CREANDO TABLA Compras EN BASE DE DATOS"
    cur.execute("DROP TABLE IF EXISTS Compras")
    cur.execute("CREATE TABLE Compras (registro INTEGER NOT NULL PRIMARY KEY UNIQUE, " +
                                       "id_comprador INTEGER NOT NULL DEFAULT ' ', " + 
                                       "id_libro INTEGER NOT NULL DEFAULT ' ')") 

def db_create():

    conn = sqlite3.connect('Libreria')
    cur = conn.cursor()

    create_books_table(cur)
    create_customers_table(cur)
    create_purchases_table(cur)
    conn.commit()
    cur.close()
    conn.close()
    
def db_setup():
    db_create()
    db_seed()
