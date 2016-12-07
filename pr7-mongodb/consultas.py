# -*- coding: utf-8 -*-

##
## INCLUIR LA CABECERA AQUI
##

from bottle import *

@get('/find_user')
def find_user():
    # http://localhost:8080/find_user?username=burgoscarla
    pass


@get('/find_users')
def find_users():
    # http://localhost:8080/find_users?name=Luz
    # http://localhost:8080/find_users?name=Luz&surname=Romero
    # http://localhost:8080/find_users?name=Luz&food=hotdog
    pass


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
