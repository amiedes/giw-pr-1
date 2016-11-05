#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""
import sqlite3
import csv

def encode(text):
    return text.encode('utf-8')

def build_insert_query(content,table):
    columns=content[0]
    marks=list()
    for i in range(len(columns)):
        marks.append("?")    
    separator=","
    marks_str=separator.join(marks)
    marks_str=" (" + marks_str + ")"
    columns_str=separator.join(columns)
    query="INSERT INTO "+table+" (" +columns_str+") Values"+marks_str
    print query
    return query

    
def execute_insert_query(content,query):
    rows=list()
    print content    
    for i in range(len(content)):
        if i==0:
            continue
        else:
            single_row=tuple(content[i])
            rows.append(single_row)
    #print rows  #esto lo he dejado solo por ver la codificacion      
    
    conn = sqlite3.connect('Libreria')
    cur = conn.cursor()
    cur.executemany(query,rows)
    msg=cur.rowcount
    print msg , "filas insertadas correctamente!!"
    cur.close()
    conn.commit()
    conn.close()
    
def seed_books_table():
    # TODO: parse db/seeds/libros.csv and insert its records into DB
    src=open("db/seeds/libros.csv") 
    pointer=csv.reader(src)
    content=list(pointer)
    table="Libros"
    query=build_insert_query(content,table)
    execute_insert_query(content,query)
    src.close()    
        
        
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
