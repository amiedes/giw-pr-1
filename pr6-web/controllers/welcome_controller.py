from bottle import route, request, template, get, static_file
from lib.authentication import Authentication, AuthenticationException


@route('/welcome')
def welcome():
    try:
        Authentication.check_session(request)
        return template('welcome.tpl')
    except AuthenticationException as ae:
        message = "You are not logged in!"
        return template('sign_in.tpl', message=message)


@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/')
