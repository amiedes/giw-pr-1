#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

import sqlite3
import os
from bottle import request, response
from models.user import User
from db.commands import db_open_connection
from db.commands import db_close_connection


class AuthenticationException(Exception):
    pass


class Authentication:

    @staticmethod
    def check_login(username, password):
        user_id = User.check_credentials(username, password)
        return user_id


    @staticmethod
    def check_session(request):

        session_id = request.get_cookie("session_id")

        if session_id is None:
            raise AuthenticationException("You need to log in!")
