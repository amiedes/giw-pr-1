# -*- coding: utf-8 -*-

import random

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

print(SaltCreator.create())
