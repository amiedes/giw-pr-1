#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

import sqlite3
import os
from models.user import User
from db.commands import db_open_connection
from db.commands import db_close_connection

class AuthenticationException(Exception):
    pass

class Authentication:

    @staticmethod
    def check_login(username, password):
        print "inside auth. class ini lib"
        user_id = User.check_credentials(username, password)
        return user_id


    @staticmethod
    def check_session(request):

        session_id = request.get_cookie("session_id")

        if session_id is None:
            raise AuthenticationException("You need to log in!")


    @staticmethod
    def create_session(request, user_id):

        request.set_cookie("session_id", user_id)


    @staticmethod
    def destroy_session(request):

        if request.get_cookie("session_id"):
            request.set_cookie("session_id", None)
