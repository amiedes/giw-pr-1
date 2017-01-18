# -*- coding: utf-8 -*-

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
