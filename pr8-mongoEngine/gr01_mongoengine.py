#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 14:38:00 2016

@author: dany
"""
from mongoengine import Connection, connect

connection=Connection()
connection.drop_database('giw mongoengine')
connection.close()

db=connection['giw mongoengine']
db=connect('giw mongoengine')
