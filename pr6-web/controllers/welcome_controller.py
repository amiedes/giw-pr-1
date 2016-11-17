from bottle import route, template, get, static_file



@route('/welcome')
def welcome():
    return template('welcome.tpl')

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/')