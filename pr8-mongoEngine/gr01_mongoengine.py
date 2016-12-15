#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 14:38:00 2016

@author: dany
"""
from mongoengine import connect,Document,StringField,ComplexDateTimeField\
                        ,ListField,EmbeddedDocumentField,ReferenceField\
                        ,CASCADE

connect('giw mongoengine')

class Tarjeta_Credito(Document):
 lop=StringField(db_field='dni',primary_key=True)# only to test

class Pedido(Document):
 lop=StringField(db_field='dni',primary_key=True)# only to test

class Usuario(Document):
    DNI = StringField(db_field='dni',primary_key=True)
    nombre = StringField(required=True)
    primer_apellido=StringField(required=True)
    segundo_apellido=StringField()
    fecha_nacimiento=StringField(required=True)
    fecha_ultimo_acceso=ComplexDateTimeField()
    tarjetas_credito=ListField(EmbeddedDocumentField(Tarjeta_Credito))
    pedidos=ListField(ReferenceField(Pedido,reverse_delete_rule=CASCADE))