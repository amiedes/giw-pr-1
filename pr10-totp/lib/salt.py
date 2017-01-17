# -*- coding: utf-8 -*-

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
