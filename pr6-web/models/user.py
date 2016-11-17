#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

import sqlite3
import os
import csv
from db.commands import db_open_connection
from db.commands import db_close_connection

class User:
    next_id = 0
    ATTRIBUTES = ['id', 'name', 'surname', 'username', 'password']
    ATTR_TYPES = {
        'id': int,
        'name': str,
        'surname': str,
        'username': str,
        'password': str,
    }

    def __init__(self, options={}):

        if 'id' in options:
            self.id = options['id']
        else:
            self.id = User.next_id
            User.next_id += 1

        self.name = options['name']
        self.surname = options['surname']
        self.username = options['username']
        self.password = options['password']

    def save(self):

        db = db_open_connection()

        db['cursor'].execute(
            "INSERT INTO users VALUES (" + self.map_attrs_for_query() + ")"
        )

        db_close_connection(db)
    #TODO hay que hacer una funcion que almacene los nuevos usuarios en el fichero csv

    def map_attrs_for_query(self):

        mapped_attrs = ""

        for idx, attr_name in enumerate(User.ATTRIBUTES):

            attr_value = getattr(self, attr_name)
            mapped_attrs += self.to_sql_str(attr_name, attr_value)

            if (idx < len(User.ATTRIBUTES) - 1):
                mapped_attrs += ", "

        return mapped_attrs

    @staticmethod
    def seed():
        csv_file = open("models/users_seed.csv")
        csv_content = csv.reader(csv_file, delimiter=';')
        headers = csv_content.next()

        for row in csv_content:
            params = {}
            for idx, attr_name in enumerate(User.ATTRIBUTES[1:]):  # skip 'id'
                params[attr_name] = row[idx]

            user = User(params)
            user.save()

        csv_file.close()

    @staticmethod
    def new(object_params):

        new_user = User(options = object_params)
        new_user.save()

    @staticmethod
    def find(filter_name, filter_value):

        db = db_open_connection()

        cursor = db['cursor'].execute("\
            SELECT username FROM users \
            WHERE " + filter_name + " = " + User.to_sql_str(filter_name, filter_value)
        )

        result_data = User.cursor_to_list(cursor)

        name = result_data[0]

        return name


    @staticmethod
    def check_credentials(username, password):

        db = db_open_connection()

        cursor = db['cursor'].execute("\
            SELECT id FROM users \
            WHERE (username = \'" + username + "\' AND password = \'" + password + "\')"
        )

        result_data = cursor.fetchone()
        db_close_connection(db)

        if result_data is None:
            return -1
        else:
            return result_data[0]


    # Transforms a cursor object into an object list, consuming the cursor in
    # the process
    @staticmethod
    def cursor_to_list(cursor):

        result_list = []

        for idx, record in enumerate(cursor):
            consulate_params = {}
            for idx, column in enumerate(record):
                consulate_params[Consulate.ATTRIBUTES[idx]] = column

            consulate = Consulate(consulate_params)
            result_list.append(consulate)

        return result_list


    @staticmethod
    def to_sql_str(field_name, field_value):
        if User.ATTR_TYPES[field_name] is str:
            return "\'" + field_value + "\'"
        else:
            return str(field_value)
