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


class Totp():

    SECRET_LENGTH = 16
    TOTP_NUMBERS = '234567'
    UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    ALPHABET = ''.join((TOTP_NUMBERS, UPPERCASE))


    def gen_secret():

        salt_chars = []

        for i in range(Totp.SECRET_LENGTH):
            salt_chars.append(random.choice(Totp.ALPHABET))

        salt_string = ''.join(salt_chars)

        return salt_string


    def gen_gauth_url(app_name, username, secret):

        return 'otpauth://totp/' + username + '?secret=' + secret + '&issuer=' + app_name


    def gen_qrcode_url(gauth_url):

        return 'https://api.qrserver.com/v1/create-qr-code/?data=' + gauth_url
