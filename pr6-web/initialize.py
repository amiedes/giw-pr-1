#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

from bottle import route, run
from controllers.consulate_controller import *
from db.commands import db_create, db_reset, db_open_connection, db_close_connection
from models.consulate import Consulate

db_reset()
Consulate.seed()

run( host = '0.0.0.0', port = 8080)
