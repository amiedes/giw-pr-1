#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""
import sqlite3

def query_1(cur):
    print "Ejecutando query_1()..."
    cur.execute("SELECT l.pais, COUNT(c.id_libro) AS 'num_libros' " +
                "FROM Libros l JOIN Compras c ON l.registro=c.id_libro " +
                "GROUP BY l.pais " +
                "ORDER BY num_libros DESC")
    for (pais, numero) in cur.fetchall():
        print pais, ": ", numero, " libros vendidos" 
    
def query_2(cur):
    print "query_2()"
    # TODO: obtener la media de los importes gastados por los compradores, agrupados por población y ordenados decrecientemente por el importe medio
    
def query_3(cur):
    print "Ejecutando query_3()..."
    cur.execute("UPDATE Compras set id_comprador = ?, id_libro = ? " +
                "WHERE registro = ?", [3, 3, 10])
    
    cur.execute("UPDATE Compras set id_comprador = ?, id_libro = ? " +
                "WHERE registro = ?", [3, 7, 11])
    print "Filas actualizadas correctamente!"
    
def query_support_price_avg(cur):
    print "Ejecutando query_support_price_avg()..."
    cur.execute("SELECT soporte, SUM(importe) AS 'total' " +
                "FROM Libros " +
                "GROUP BY soporte")
    for (soporte, tot) in cur.fetchall():
        print soporte, ": ", tot

def query_delete_inactive_customers(cur):
    print "Ejecutando query_delete_inactive_customers()..."
    cur.execute("DELETE FROM Compradores " +
                "WHERE Compradores.registro NOT IN " +
                    "(SELECT DISTINCT id_comprador FROM Compras)" )
    print "Filas borradas correctamente!"

def db_run_all_queries():
    conn = sqlite3.connect('Libreria')
    cur = conn.cursor()
    query_1(cur)
    query_2(cur)
    query_3(cur)
    query_support_price_avg(cur)
    query_delete_inactive_customers(cur)
    conn.commit()
    cur.close()
    conn.close()
