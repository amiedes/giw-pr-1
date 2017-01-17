# -*- coding: utf-8 -*-

from mongoengine import *
from lib.salt import *

class PasswordMatchError(Exception):
    pass

class InvalidNickname(Exception):
    pass

class User(Document):

    nickname = StringField(primary_key=True)

    name = StringField(required=True)

    country = StringField(required=True)

    email = StringField(required=True)

    encrypted_password = StringField(required=True)

    salt = StringField()


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

    def check_password(nickname, password):

        query_set = User.objects(nickname=nickname)

        if (len(query_set) == 0):
            raise InvalidNickname('El usuario no existe')

        user = query_set[0]

        given_encrypted_pwd = PasswordEncrypter.encrypt(password, user.salt)

        if (user.encrypted_password != given_encrypted_pwd):
            raise PasswordMatchError('Contraseña incorrecta')

        return user
