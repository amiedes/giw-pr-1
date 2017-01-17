# -*- coding: utf-8 -*-

#
# CABECERA AQUI
#


from bottle import *
from mongoengine import *
from models.user import *

##############
# APARTADO 1 #
##############

#
# Explicación detallada del mecanismo escogido para el almacenamiento de c
# contraseñas, explicando razonadamente por qué es seguro
#


@post('/signup')
def signup():

    try:
        connect('giw')

        nickname = request.forms.get('nickname')
        password = request.forms.get('password')
        password2 = request.forms.get('password2')

        if len(User.objects(nickname=nickname)) != 0:
            message = 'El nickname no está disponible'
            raise Error()

        if (password != password2):
            message = 'Las contraseñas no coinciden'
            raise Error()

        user = User(
            nickname = nickname,
            name = request.forms.get('name'),
            country = request.forms.get('country'),
            email = request.forms.get('email'),
            password = password
        )

        user.save()

        message = 'Bienvenido usuario ' + user.name

    except ValidationError as error:
        message = 'Validation error prevented this record from being saved into the database.'
    except:
        message = 'An error occurred while performing the requested action'
    finally:
        return template('signup.tpl', message=message)


@post('/change_password')
def change_password():
    pass


@post('/login')
def login():
    pass


##############
# APARTADO 2 #
##############


def gen_secret():
    # >>> gen_secret()
    # '7ZVVBSKR22ATNU26'
    pass


def gen_gauth_url(app_name, username, secret):
    # >>> gen_gauth_url( 'GIW_grupoX', 'pepe_lopez', 'JBSWY3DPEHPK3PXP')
    # 'otpauth://totp/pepe_lopez?secret=JBSWY3DPEHPK3PXP&issuer=GIW_grupoX
    pass


def gen_qrcode_url(gauth_url):
    # >>> gen_qrcode_url('otpauth://totp/pepe_lopez?secret=JBSWY3DPEHPK3PXP&issuer=GIW_grupoX')
    # 'http://api.qrserver.com/v1/create-qr-code/?data=otpauth%3A%2F%2Ftotp%2Fpepe_lopez%3Fsecret%3DJBSWY3DPEHPK3PXP%26issuer%3DGIW_grupoX'
    pass



@post('/signup_totp')
def signup_totp():
    pass


@post('/login_totp')
def login_totp():
    pass


if __name__ == "__main__":
    # NO MODIFICAR LOS PARÁMETROS DE run()
    run(host='localhost',port=8080,debug=True)