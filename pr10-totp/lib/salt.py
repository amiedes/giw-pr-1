# -*- coding: utf-8 -*-

"""
Autores: Daniel Reyes, Ania Pietrzak, Alberto Miedes
Asignatura: Gestión de Información en la Web (GIW) - Práctica 10 - Grupo 1

Daniel Reyes, Ania Pietrzak y Alberto Miedes declaramos que esta solución es
fruto exclusivamente de nuestro trabajo personal. No hemos sido ayudados por
ninguna otra persona ni hemos obtenido la solución de fuentes externas, y
tampoco hemos compartido nuestra solución con nadie. Declaramos además que no
hemos realizado de manera deshonesta ninguna otra actividad que pueda mejorar
nuestros resultados ni perjudicar los resultados de los demás.
"""

import random
import hashlib

class SaltCreator():

    SALT_LENGTH = 64
    NUMBERS   = '0123456789'
    LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
    UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    SYMBOLS   = "!@#$%&/()=?¿¡^*+[]¨,;.-_<>"

    ALPHABET = ''.join((NUMBERS, LOWERCASE, UPPERCASE, SYMBOLS))

    def create():

        salt_chars = []

        for i in range(SaltCreator.SALT_LENGTH):
            salt_chars.append(random.choice(SaltCreator.ALPHABET))

        salt_string = ''.join(salt_chars)

        return salt_string

class PasswordEncrypter():

    def encrypt(password, salt):

        salted_password = (password + salt).encode('utf-8')

        return hashlib.sha512(salted_password).hexdigest()
