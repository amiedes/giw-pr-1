#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

import sqlite3
import os
import csv
from db.commands import db_open_connection
from db.commands import db_close_connection


class Consulate:
    next_id = 0
    ATTRIBUTES = ['id', 'name', 'postal_code', 'neighborhood', 'district', 'latitude', 'longitude']
    ATTR_TYPES = {
        'id': int,
        'name': str,
        'postal_code': int,
        'neighborhood': str,
        'district': str,
        'latitude': float,
        'longitude': float
    }


    def __init__(self, options={}):

        if 'id' in options:
            self.id = options['id']
        else:
            self.id = Consulate.next_id
            Consulate.next_id += 1

        self.name = options['name']
        self.postal_code = options['postal_code']
        self.neighborhood = options['neighborhood']
        self.district = options['district']
        self.latitude = options['latitude']
        self.longitude = options['longitude']


    def save(self):

        db = db_open_connection()

        db['cursor'].execute(
            "INSERT INTO consulates VALUES (" + self.map_attrs_for_query() + ")"
        )

        db_close_connection(db)


    def destroy(self):

        db = db_open_connection()

        db['cursor'].execute(
            "DELETE FROM consulates WHERE id = " + str(self.id)
        )

        db_close_connection(db)
    
    def modify(self, object_params, requested_id):

        
        db = db_open_connection()
        claves = object_params.keys()
        columnas = ''
        for clave in claves:
            columnas = columnas + str(clave) + '=?, '
        columnas = columnas[:-2]
        sql = "UPDATE consulates SET " + columnas + " WHERE id=?"

        values = object_params.values()
        values.append(requested_id)

        db['cursor'].execute(sql, values)
                
        db_close_connection(db)            

    def map_attrs_for_query(self):

        mapped_attrs = ""

        for idx, attr_name in enumerate(Consulate.ATTRIBUTES):

            attr_value = getattr(self, attr_name)
            mapped_attrs += self.to_sql_str(attr_name, attr_value)

            if (idx < len(Consulate.ATTRIBUTES) - 1):
                mapped_attrs += ", "

        return mapped_attrs


    @staticmethod
    def new(object_params):

        new_consulate = Consulate(options = object_params)
        new_consulate.save()


    @staticmethod
    def find(filter_name, filter_value):

        db = db_open_connection()

        cursor = db['cursor'].execute("\
            SELECT * FROM consulates \
            WHERE " + filter_name + " = " + Consulate.to_sql_str(filter_name, filter_value)
        )
        result_data = Consulate.cursor_to_list(cursor)

        db_close_connection(db)

        return result_data


    @staticmethod
    def all():

        db = db_open_connection()

        cursor = db['cursor'].execute("SELECT * FROM consulates")
        result_data = Consulate.cursor_to_list(cursor)

        db_close_connection(db)

        return result_data


    @staticmethod
    def seed():

        csv_file = open("models/consulates_seed.csv")
        csv_content = csv.reader(csv_file, delimiter=';')
        headers = csv_content.next()

        for row in csv_content:
            params = {}
            for idx, attr_name in enumerate(Consulate.ATTRIBUTES[1:]):  # skip 'id'
                params[attr_name] = row[idx]

            consulate = Consulate(params)
            consulate.save()

        csv_file.close()


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
        if Consulate.ATTR_TYPES[field_name] is str:
            return "\'" + field_value + "\'"
        else:
            return str(field_value)
            
