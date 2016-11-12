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
    attributes = ['id', 'name', 'postal_code', 'neighborhood', 'district', 'latitude', 'longitude']


    def __init__(self, options={}):

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


    def map_attrs_for_query(self):

        mapped_attrs = ""

        for idx, attr_name in enumerate(Consulate.attributes):
            attr_value = getattr(self, attr_name)
            if type(attr_value) is str:
                mapped_attrs += ("\'" + attr_value + "\'")
            else:
                mapped_attrs += str(attr_value)
            if (idx < len(Consulate.attributes) - 1):
                mapped_attrs += ", "

        return mapped_attrs


    @staticmethod
    def all():

        db = db_open_connection()

        cursor = db['cursor'].execute("SELECT * FROM consulates")
        result_data = Consulate.parse_cursor(cursor)

        db_close_connection(db)

        return result_data


    @staticmethod
    def seed():

        csv_file = open("models/consulates_seed.csv")
        csv_content = csv.reader(csv_file, delimiter=';')
        headers = csv_content.next()

        for row in csv_content:
            params = {}
            for idx, attr_name in enumerate(Consulate.attributes[1:]):  # skip 'id'
                params[attr_name] = row[idx]

            consulate = Consulate(params)
            consulate.save()

        csv_file.close()


    # Transforms a cursor object into a dictionary list, consuming the cursor in
    # the process
    @staticmethod
    def parse_cursor(cursor):

        result_list = []

        for idx, record in enumerate(cursor):
            consulate = {}
            for idx, column in enumerate(record):
                consulate[Consulate.attributes[idx]] = column
            result_list.append(consulate)

        return result_list
