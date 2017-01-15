# -*- coding: utf-8 -*-

from mongoengine import *

class User(Document):

    nickname = StringField(primary_key=True)

    name = StringField(required=True)

    country = StringField(required=True)

    email = StringField(required=True)

    password = StringField(required=True)
