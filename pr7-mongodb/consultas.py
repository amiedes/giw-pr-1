# -*- coding: utf-8 -*-

"""
Autores: Daniel Reyes, Ania Pietrzak, Alberto Miedes
Asignatura: Gestión de Información en la Web (GIW) - Práctica 7 - Grupo 1

Daniel Reyes, Ania Pietrzak y Alberto Miedes declaramos que esta solución es
fruto exclusivamente de nuestro trabajo personal. No hemos sido ayudados por
ninguna otra persona ni hemos obtenido la solución de fuentes externas, y
tampoco hemos compartido nuestra solución con nadie. Declaramos además que no
hemos realizado de manera deshonesta ninguna otra actividad que pueda mejorar
nuestros resultados ni perjudicar los resultados de los demás.
"""

from bottle import *
from pymongo import *
from app.models.address import Address
from app.models.credit_card import CreditCard
from app.models.user import User
from app.exceptions.invalid_parameters_error import InvalidParametersError

# http://localhost:8080/find_user?username=burgoscarla
@get('/find_user')
def find_user():

    connection = MongoClient('localhost', 27017)
    db = connection.giw
    usuarios = db.usuarios

    user_record = usuarios.find({'_id': request.query['username']})
    user = User(user_record[0])

    return template('find_user.tpl', user=user)


# http://localhost:8080/find_users?name=Luz
# http://localhost:8080/find_users?name=Luz&surname=Romero
# http://localhost:8080/find_users?name=Luz&food=hotdog
@get('/find_users')
def find_users():
    try:
        try:
            for param in request.query:
                User.valid_parameters()[param]
        except KeyError:
            raise InvalidParametersError()

        connection = MongoClient('localhost', 27017)
        db = connection.giw
        users = db.usuarios

        cursor = users.find(request.query)
        matched_users = []

        for record in cursor:
            user = User.build_from_db_record(record)
            matched_users.append(user)

        return template('users_collection.tpl', users = matched_users, matches = len(matched_users))

    except InvalidParametersError:
        return template('error_template.tpl', message = 'Invalid parameters')


@get('/find_users_or')
def find_users_or():
    # http://localhost:8080/find_users_or?name=Luz&surname=Corral
    pass


@get('/find_like')
def find_like():
    # http://localhost:8080/find_like?like=football
    pass


@get('/find_country')
def find_country():
    # http://localhost:8080/find_country?country=Irlanda
    pass


@get('/find_email_birthdate')
def email_birthdate():
    # http://localhost:8080/find_email_birthdate?from=1973-01-01&to=1990-12-31
    pass


# http://localhost:8080/find_country_likes_limit_sorted?country=Irlanda&likes=movies,animals&limit=4&ord=asc
@get('/find_country_likes_limit_sorted')
def find_country_likes_limit_sorted():

    connection = MongoClient('localhost', 27017)
    db = connection.giw
    users = db.usuarios

    # parse query parameters
    country = request.query['country']
    likes = request.query['likes'].split(',')
    limit = int(request.query['limit'])
    order = (1 if request.query['ord'] == 'asc' else -1)

    filter_hash = {
        'address.country': country,
        'likes': { '$all': likes }
    }

    cursor = users.find(filter_hash).sort('birthdate', order).limit(limit)
    matched_users = []

    for record in cursor:
        user = User.build_from_db_record(record)
        matched_users.append(user)

    return template('users_collection.tpl', users = matched_users, matches = len(matched_users))


if __name__ == "__main__":
    # No cambiar host ni port ni debug
    run(host='localhost',port=8080,debug=True)
