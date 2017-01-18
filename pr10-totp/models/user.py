# -*- coding: utf-8 -*-

"""
Autores: Daniel Reyes, Ania Pietrzak, Alberto Miedes
Asignatura: Gestión de Información en la Web (GIW) - Práctica 10 - Grupo 1

Daniel Reyes, Ania Pietrzak y Alberto Miedes declaramos que esta solución es
fruto exclusivamente de nuestro trabajo personal. No hemos sido ayudados por
ninguna otra persona ni hemos obtenido la solución de fuentes externas, y
tampoco hemos compartido nuestra solución con nadie. Declaramos además que no
hemos realizado de manera deshonesta ninguna otra actividad que pueda mejorar
nuestros resultados ni perjudicar los resultados de los demás.
"""

from mongoengine import *
from lib.salt import *

class PasswordMatchError(Exception):
    pass

class InvalidNickname(Exception):
    pass

class User(Document):

    meta = {'collection': 'users'}

    nickname            = StringField(primary_key=True)
    name                = StringField(required=True)
    country             = StringField(required=True)
    email               = StringField(required=True)
    encrypted_password  = StringField(required=True)
    salt                = StringField()
    totp_salt           = StringField()


    def salt_and_save(params={}):

        salt = SaltCreator.create()
        encrypted_password = PasswordEncrypter.encrypt(params['password'], salt)

        user = User(
            nickname = params['nickname'],
            name = params['name'],
            country = params['country'],
            email = params['email'],
            encrypted_password = encrypted_password,
            salt = salt
        )

        return user.save()

    def totp_save(params={}):

        salt = SaltCreator.create()
        encrypted_password = PasswordEncrypter.encrypt(params['password'], salt)

        user = User(
            nickname = params['nickname'],
            name = params['name'],
            country = params['country'],
            email = params['email'],
            encrypted_password = encrypted_password,
            totp_salt = params['totp_salt']
        )

        return user.save()


    def check_password(nickname, password):

        query_set = User.objects(nickname=nickname)

        if (len(query_set) == 0):
            raise InvalidNickname('El usuario no existe')

        user = query_set[0]

        given_encrypted_pwd = PasswordEncrypter.encrypt(password, user.salt)

        if (user.encrypted_password != given_encrypted_pwd):
            raise PasswordMatchError('Contraseña incorrecta')

        return user
