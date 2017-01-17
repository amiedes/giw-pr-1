# -*- coding: utf-8 -*-

import hashlib
from mongoengine import *
from lib.salt_creator import *

class User(Document):

    nickname = StringField(primary_key=True)

    name = StringField(required=True)

    country = StringField(required=True)

    email = StringField(required=True)

    encrypted_password = StringField(required=True)

    salt = StringField()


    def salt_and_save(params={}):

        salt = SaltCreator.create()

        pwd_with_salt = (params['password'] + salt).encode('utf-8')
        encrypted_password = hashlib.sha512(pwd_with_salt).hexdigest()

        user = User(
            nickname = params['nickname'],
            name = params['name'],
            country = params['country'],
            email = params['email'],
            encrypted_password = encrypted_password,
            salt = salt
        )

        return user.save()
