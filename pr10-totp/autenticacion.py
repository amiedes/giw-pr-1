# -*- coding: utf-8 -*-

#
# CABECERA AQUI
#


from bottle import *
from mongoengine import *
from models.user import *
from lib.salt import *
from lib.totp import *

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
            raise InvalidNickname()

        if (password != password2):
            raise PasswordMatchError()

        user = User.salt_and_save({
            'nickname': nickname,
            'name': request.forms.get('name'),
            'country': request.forms.get('country'),
            'email': request.forms.get('email'),
            'password': password
        })

        message = 'Bienvenido usuario ' + user.name + '.'

    except InvalidNickname:
        message = 'El alias de usuario ya existe.'
    except PasswordMatchError:
        message = 'Las contraseñas no coinciden.'
    except ValidationError:
        message = 'Validation error prevented this record from being saved into the database.'
    except:
        message = 'An error occurred while performing the requested action'
    finally:
        return template('template.tpl', message=message)


@post('/change_password')
def change_password():
    try:
        connect('giw')

        nickname = request.forms.get('nickname')
        old_password = request.forms.get('old_password')
        new_password = request.forms.get('new_password')

        user = User.check_password(nickname, old_password)

        salt = SaltCreator.create()
        encrypted_password = PasswordEncrypter.encrypt(new_password, salt)

        user.salt = salt
        user.encrypted_password = encrypted_password

        user.save()

        message = 'La contraseña del usuario ' + user.name + ' ha sido modificada.'

    except InvalidNickname:
        message = 'Usuario o contraseña incorrectos.'
    except PasswordMatchError:
        message = 'Usuario o contraseña incorrectos.'
    except:
        message = 'An error occurred while performing the requested action'
    finally:
        return template('template.tpl', message=message)

@post('/login')
def login():
    try:
        connect('giw')

        nickname = request.forms.get('nickname')
        password = request.forms.get('password')

        user = User.check_password(nickname, password)

        message = 'Bienvenido ' + user.name

    except InvalidNickname:
        message = 'Usuario o contraseña incorrectos.'
    except PasswordMatchError:
        message = 'Usuario o contraseña incorrectos.'
    except:
        message = 'An error occurred while performing the requested action'
    finally:
        return template('template.tpl', message=message)


##############
# APARTADO 2 #
##############


def gen_secret():

    return Totp.gen_secret()


def gen_gauth_url(app_name, username, secret):

    return Totp.gen_gauth_url(app_name, username, secret)


def gen_qrcode_url(gauth_url):

    return Totp.gen_qrcode_url(gauth_url)


@post('/signup_totp')
def signup_totp():

    try:
        connect('giw')

        nickname = request.forms.get('nickname')
        password = request.forms.get('password')
        password2 = request.forms.get('password2')

        if len(User.objects(nickname=nickname)) != 0:
            raise InvalidNickname()

        if (password != password2):
            raise PasswordMatchError()

        # En otro caso insertará al usuario en la colección users y devolverá una
        # página web con el código QR para configurar Google Authenticator. Esta
        # página web contendrá también el nombre de usuario y la semilla generada
        # por si el usuario quiere configurar Google Authenticator manualmente o
        # utilizar otra aplicación TOTP.

        secret = Totp.gen_secret()
        gauth_url = Totp.gen_gauth_url('GIW_grupo1', nickname, secret)
        qrcode_url = Totp.gen_qrcode_url(gauth_url)

        user = User.totp_save({
            'nickname': nickname,
            'name': request.forms.get('name'),
            'country': request.forms.get('country'),
            'email': request.forms.get('email'),
            'password': password,
            'totp_salt': secret
        })

        return template('totp.tpl', qrcode_url=qrcode_url, username=user.name, secret=user.totp_salt)

    except InvalidNickname:
        message = 'El alias de usuario ya existe.'
    except PasswordMatchError:
        message = 'Las contraseñas no coinciden.'
    except ValidationError:
        message = 'Validation error prevented this record from being saved into the database.'
    except:
        message = 'An error occurred while performing the requested action'
    finally:
        return template('template.tpl', message=message)


@post('/login_totp')
def login_totp():
    pass


if __name__ == "__main__":
    # NO MODIFICAR LOS PARÁMETROS DE run()
    run(host='localhost',port=8080,debug=True)
