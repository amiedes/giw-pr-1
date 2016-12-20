#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autores: Daniel Reyes, Ania Pietrzak, Alberto Miedes
Asignatura: Gestión de Información en la Web (GIW) - Práctica 7 - Grupo 1

Daniel Reyes, Ania Pietrzak y Alberto Miedes declaramos que esta solución es
fruto exclusivamente de nuestro trabajo personal. No hemos sido ayudados por
ninguna otra persona ni hemos obtenido la solución de fuentes externas, y
tampoco hemos compartido nuestra solución con nadie. Declaramos además que no
hemos realizado de manera deshonesta ninguna otra actividad que pueda mejorar
nuestros resultados ni perjudicar los resultados de los demás.
"""

from mongoengine import connect,Document,StringField,ComplexDateTimeField\
                        ,ListField,EmbeddedDocumentField,ReferenceField\
                        ,EmbeddedDocument,PULL,ValidationError

connect('giw mongoengine')

#-----------------PRODUCTOS---------------------------------------
class Producto(Document):
    # er: numero de 13 digitos
    codigo=StringField(primary_key=True,regex='\d{13}$')
    
    nombre=StringField(required=True)
    
    # er: combinacion de digitos --> Natural
    categoria=StringField(required=True,regex='\d*$')
    
    # er: combinacion de digitos --> Natural
    subcategoria=ListField(StringField(),regex='\d*$')   
    
    def clean(self):
        #comprobar si tiene lista de categorias secundarias
        if len(self.subcategoria) > 0:
            #anadir categoria como primer elemento de subcategoria si todavia no aparace
            if self.subcategoria[0] != self.categoria:
                self.subcategoria.append(0, self.categoria)
    
    
#---------------LINEAS DE PEDIDO-----------------------------------    
class Linea_Pedido(EmbeddedDocument):
    # er: combinacion de digitos --> Natural
    cantidad_productos=StringField(required=True,regex='\d*$')
    
    # er: float con dos cifras decimales
    precio_unidad=StringField(required=True,regex='\d*\.\d{2}$')
    nombre_producto=StringField(required=True)
    
    # er: float con dos cifras decimales
    precio_total=StringField(required=True,regex='\d*\.\d{2}$')
    producto=ReferenceField(Producto)    
    
    def clean(self):
        #comprobar nombre de producto
        nombre=self.nombre_producto
        nombre_real=self.producto.nombre
        if(nombre_real != nombre):
            raise ValidationError("ERROR: Nombre de Producto Erroneo")
        
        #comprobar precio total de linea
        total=float(self.precio_total)
        cantidad=int(self.cantidad_productos)
        precio_unidad=float(self.precio_unidad)
        total_calculado=cantidad*precio_unidad    
        if(total != total_calculado):    
            raise ValidationError("ERROR: Precio de linea Mal Calculado")

    
    
#--------------------------PEDIDOS---------------------------------    
class Pedido(Document):
    # er: float con dos cifras decimales:
    total=StringField(required=True,regex='\d*\.\d{2}$')
    fecha=ComplexDateTimeField(required=True)
    lineas_pedido=ListField(EmbeddedDocumentField(Linea_Pedido,required=True)\
                            ,required=True)
    def clean(self):
        total=float(self.total)
        total_from_lines=0.00
        i=0
        for i in range(len(self.lineas_pedido)):
            total_linea=float(self.lineas_pedido[i].precio_total)
            total_from_lines=total_from_lines+total_linea
            
        if(total != total_from_lines):    
            raise ValidationError("ERROR: No concuerdan los totales")

            
            
    
#------------------------TARJETA DE CREDITO------------------------    
class Tarjeta_Credito(EmbeddedDocument):
    propietario=StringField(required=True)
    
    # er: 16 digitos
    numero=StringField(regex='\d{16}$',required=True)
    
    #er: c/mes debe es de la forma "0X" o bien "1Y" con rango [01-12]
    mes_caducidad=StringField(regex='0[1-9]$|1[0-2]$',required=True)
    
    # er: años definidos desde 17 hasta 29
    anio_caducidad=StringField(regex='1[7-9]$|2[0-9]$',required=True)
    
    # er: 3 digitos
    cvv=StringField(max_length=3,regex='\d{3}$',required=True)



    
#---------------------------USUARIOS------------------------------ 
class Usuario(Document):
    # er: 1 digito o letra('X','Y','Z') + 7 digitos + 
    #     1 letra mayuscula o minuscula
    dni = StringField(primary_key=True,\
                      regex='(\d{8}|[X-Z]\d{7})[A-Z]$|'\
                          + '(\d{8}|[x-z]\d{7})[a-z]$')
    nombre = StringField(required=True)
    primer_apellido=StringField(required=True)
    segundo_apellido=StringField()
    
    # er: Rangos de fecha [1900-2017]-[01-12]-[01-31] 
    fecha_nacimiento=StringField(required=True,\
                                 regex='(19\d{2}-|20[0-1][0-7]-)'\
                                 + '(0[1-9]-|1[0-2]-)'\
                                 + '(0[1-9]$|(1|2)\d{1}$|3[0-1]$)'\
                                 )
    fecha_ultimo_acceso=ComplexDateTimeField()
    tarjetas_credito=ListField(EmbeddedDocumentField(Tarjeta_Credito))
    pedidos=ListField(ReferenceField(Pedido,reverse_delete_rule=PULL))
    #creo que esta linea hace el ejercicio 7 REVISAR
    
  #---- verificacion de DNI o NIE: ----
    def clean(self):
        letras=['T','R','W','A','G','M','Y','F','P','D','X','B',\
                'N','J','Z','S','Q','V','H','L','C','K','E' ]
        dni=self.dni.upper()
        id_number=0
        offset=0
        last_letter=dni[len(dni)-1]
        # calcular offset en caso de NIE
        if(dni[0].isalpha() and dni[0]!='X'):
            offset=offset+10000000
            if(dni[0]=='Z'):
                offset=offset+10000000
        else:
            offset=0
            
        # obtener la cifra para calcular el digito de control    
        dni=''
        i=0
        for i in range(len(self.dni)):
            if(self.dni[i].isalpha()):
                continue
            else:
                dni=dni+self.dni[i]
        id_number=int(dni)
        id_number=id_number+offset

        #calculo y comprobacion
        correct_index=id_number%23
        correct_letter=letras[correct_index] 
        if(correct_letter != last_letter):
            raise ValidationError("El DNI o NIE introducido No Existe")
#------------------------------------------------------------------------