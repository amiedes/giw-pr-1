# -*- coding: utf-8 -*-

##
## INCLUIR LA CABECERA AQUI
##

from bottle import *
from pymongo import *

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
    pass


@get('/age_range')
# http://localhost:8080/age_range?min=80
def agg3():
    pass


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
