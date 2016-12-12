# -*- coding: utf-8 -*-

##
## INCLUIR LA CABECERA AQUI
##

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
            user = User(record)
            user.credit_card = CreditCard({
                'expire_year': record['credit_card']['expire']['year'],
                'expire_month': record['credit_card']['expire']['month'],
                'number': record['credit_card']['number']
            })
            user.address = Address({
                'country': record['address']['country'],
                'zip': record['address']['zip'],
                'street': record['address']['street'],
                'num': record['address']['num'],
            })
            print "ADDRESS:"
            print user.address.pretty()
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


@get('/find_country_likes_limit_sorted')
def find_country_likes_limit_sorted():
    # http://localhost:8080/find_country_likes_limit_sorted?country=Irlanda&likes=movies,animals&limit=4&ord=asc
    pass


if __name__ == "__main__":
    # No cambiar host ni port ni debug
    run(host='localhost',port=8080,debug=True)
