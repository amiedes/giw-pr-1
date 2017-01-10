# -*- coding: utf-8 -*-

##
## INCLUIR LA CABECERA AQUI
##

from bottle import *
from pymongo import *
from bson.son import SON

@get('/top_countries')
# http://localhost:8080/top_countries?n=3
def agg1():

    connection = MongoClient('localhost', 27017)
    db = connection.giw

    n_countries = request.query['n']

    cursor = db['usuarios'].aggregate(
        [
            { '$group': { '_id': '$pais', 'count': { '$sum': 1 } } },
            { '$sort': { 'count': -1, '_id': 1 } },
            { '$limit': int(n_countries) }
        ]
    )

    top_countries = []
    for record in cursor:
        top_countries.append(record)

    connection.close()

    return template('agg1.tpl', top_countries=top_countries)


@get('/products')
# http://localhost:8080/products?min=2.34
def agg2():

    connection = MongoClient('localhost', 27017)
    db = connection.giw

    min_price = request.query['min']

    cursor = db['pedidos'].aggregate(
        [
            { '$unwind': '$lineas' },
            { '$match': { "lineas.precio": { '$gt': float(min_price) } } },
            { '$group': { '_id': '$lineas.nombre', 'count': { '$sum': 1 }, 'precio': { '$first': '$lineas.precio' } } },
            { '$project': { '_id': 0, 'nombre_producto': '$_id', 'num_ventas': '$count', 'precio_unitario': '$precio' } }
        ]
    )

    products_ranking = []
    for record in cursor:
        products_ranking.append(record)

    connection.close()

    return template('agg2.tpl', products_ranking=products_ranking)


@get('/age_range')
# http://localhost:8080/age_range?min=80
def agg3():

    connection = MongoClient('localhost', 27017)
    db = connection.giw

    min_usrs = request.query['min']

    cursor = db['usuarios'].aggregate(
        [
            { '$group': { '_id': '$pais', 'count': { '$sum': 1 }, 'edad_min': { '$min': '$edad' }, 'edad_max': { '$max': '$edad' } } },
            { '$project': { '_id': 0, 'pais': '$_id', 'num_usuarios': '$count', 'rango_edades': { '$subtract': [ '$edad_max', '$edad_min' ] } } },
            { '$match': { 'num_usuarios': { '$gt': int(min_usrs) } } },
            { '$sort': SON(
                            [ ('rango_edades', -1), ('pais', 1) ]
                          )
            }
        ]
    )

    countries = []
    for record in cursor:
        countries.append(record)

    connection.close()

    return template('agg3.tpl', countries=countries)


@get('/avg_lines')
# http://localhost:8080/avg_lines
def agg4():
    pass


@get('/total_country')
# http://localhost:8080/total_country?c=Alemania
def agg5():
    pass


if __name__ == "__main__":
    # No cambiar host ni port ni debug
    run(host='localhost',port=8080,debug=True)
