#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

import sqlite3
import csv


#--------------------------------------------------
# Generic Functions to Insert
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
    
    conn = sqlite3.connect('Libreria')
    conn.text_factory = str
    cur = conn.cursor()
    cur.executemany(query,rows)
    msg=cur.rowcount
    print msg , "Filas insertadas correctamente!! \n" #puedes ver que se inserta
    cur.close()
    conn.commit()
    conn.close()

    
#------------------------------------------------------
#Specific Functions to insert in every table    
def seed_books_table():
    src=open("db/seeds/libros.csv") 
    pointer=csv.reader(src)
    content=list(pointer)
    table="Libros"
    query=build_insert_query(content,table)
    execute_insert_query(content,query)
    src.close()    
        
        
def seed_customers_table():
    src=open("db/seeds/compradores.csv") 
    pointer=csv.reader(src)
    content=list(pointer)
    table="Compradores"
    query=build_insert_query(content,table)
    execute_insert_query(content,query)
    src.close()    
    

def seed_purchases_table():
    src=open("db/seeds/compras.csv") 
    pointer=csv.reader(src)
    content=list(pointer)
    table="Compras"
    query=build_insert_query(content,table)
    execute_insert_query(content,query)
    src.close()    

    
#-----------------------------
# Principal Call    
def db_seed():
    seed_books_table()
    seed_customers_table()
    seed_purchases_table()
