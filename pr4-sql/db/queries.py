#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""
import sqlite3

def query_1(cur):
    print "\nEjecutando query_1()...\n"
    
    cur.execute("SELECT l.pais, COUNT(c.id_libro) AS 'num_libros' " +
                "FROM Libros l JOIN Compras c ON l.registro=c.id_libro " +
                "GROUP BY l.pais " +
                "ORDER BY num_libros DESC")

    for (pais, numero) in cur.fetchall():
        print pais + ": ", numero, " libros vendidos"

def query_2(cur):
    print "\nEjecutando query_2()...\n"

    cur.execute(
    "   SELECT poblacion, AVG(importe) AS importe_medio                        \
        FROM (Compradores u JOIN Compras c ON (u.registro = c.id_comprador))   \
            JOIN Libros l ON (c.id_libro = l.registro)                         \
        GROUP BY poblacion                                                     \
        ORDER BY importe_medio DESC                                            \
    ")

    for(poblacion, importe_medio) in cur.fetchall():
        print poblacion + ": " + str(importe_medio)

def query_update_purchases(cur):
    print "\nEjecutando query_3()...\n"

    cur.execute("UPDATE Compras set id_comprador = ?, id_libro = ? " +
                "WHERE registro = ?", [3, 3, 10])

    cur.execute("UPDATE Compras set id_comprador = ?, id_libro = ? " +
                "WHERE registro = ?", [3, 7, 11])

    print "Filas actualizadas correctamente!"

def query_support_price_avg(cur):
    cur.execute("SELECT soporte, SUM(importe) AS 'total' " +
    print "\nEjecutando query_support_price_avg()...\n"

                "FROM Libros " +
                "GROUP BY soporte")

    for (soporte, tot) in cur.fetchall():
        print soporte, ": ", tot

def query_delete_inactive_customers(cur):
    print "\nEjecutando query_delete_inactive_customers()...\n"

    cur.execute("DELETE FROM Compradores " +
                "WHERE Compradores.registro NOT IN " +
                    "(SELECT DISTINCT id_comprador FROM Compras)" )

    print "Filas borradas correctamente!"

def db_run_all_queries():

    # connect to the database and get a cursor object
    conn = sqlite3.connect('Libreria')
    cur = conn.cursor()

    # run all queries
    query_1(cur)
    query_2(cur)
    query_update_purchases(cur)
    query_support_price_avg(cur)
    query_delete_inactive_customers(cur)

    # commit changes and close connection
    conn.commit()
    cur.close()
    conn.close()
