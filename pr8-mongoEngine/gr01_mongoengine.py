#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 14:38:00 2016

@author: dany
"""

#'''
from mongoengine import connect,Document,StringField,ComplexDateTimeField\
                        ,ListField,EmbeddedDocumentField,ReferenceField\
                        ,EmbeddedDocument,CASCADE,ValidationError

connect('giw mongoengine')


class Tarjeta_Credito(EmbeddedDocument):
    propietario=StringField(required=True)
    numero=StringField(regex='\d{16}$',required=True)
    
    #cada mes debe ser de la forma "0X" o bien "1Y" con rango [01-12]
    mes_caducidad=StringField(regex='0[1-9]$|1[0-2]$',required=True)
    
    #años definidos desde 17 hasta 29
    anio_caducidad=StringField(regex='1[7-9]$|2[0-9]$',required=True)
    cvv=StringField(max_length=3,regex='\d{3}$',required=True)
    

    
class Pedido(Document):
    lop=StringField(db_field='dni',primary_key=True)# only to test


    
class Usuario(Document):
    # 1 digito o letra('X','Y','Z') + 7 digitos + 1 letra mayuscula o minuscula
    dni = StringField(primary_key=True,\
                      regex='(\d{8}|[X-Z]\d{7})[A-Z]$|'\
                          + '(\d{8}|[x-z]\d{7})[a-z]$')
    nombre = StringField(required=True)
    primer_apellido=StringField(required=True)
    segundo_apellido=StringField()
    
    # Rangos de fecha: [1900-2017]-[01-12]-[01-31] 
    fecha_nacimiento=StringField(required=True,\
                                 regex='(19\d{2}-|20[0-1][0-7]-)'\
                                 + '(0[1-9]-|1[0-2]-)'\
                                 + '(0[1-9]$|(1|2)\d{1}$|3[0-1]$)'\
                                 )
    fecha_ultimo_acceso=ComplexDateTimeField()
    tarjetas_credito=ListField(EmbeddedDocumentField(Tarjeta_Credito))
    pedidos=ListField(ReferenceField(Pedido,reverse_delete_rule=CASCADE))

    def clean(self):
        letras=['T','R','W','A','G','M','Y','F','P','D','X','B',\
                'N','J','Z','S','Q','V','H','L','C','K','E' ]
        dni=self.dni.upper()
        id_number=0
        offset=0
        # calcular offset en caso de NIE
        if(self.dni[0].isalpha() and self.dni[0]!='X'):
            offset=offset+10000000
            if(self.dni[0]=='Z'):
                offset=offset+10000000
        else:
            offset=0
            
        # obtener la cifra para calcular el digito de control    
        dni=''
        i=0
        for i in range(len(dni)):
            if(self.dni[i].isalpha()):
                continue
            else:
                dni=dni+self.dni[i]
        id_number=int(dni)
        id_number=id_number+offset

        #calculo y comprobacion
        dni=self.dni.upper()
        last_letter=dni[len(dni)-1]
        correct_index=id_number%23
        correct_letter=letras[correct_index] 
        if(correct_letter != last_letter):
            raise ValidationError("El DNI o NIE introducido No Existe")
