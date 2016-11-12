from bottle import route, template


@route('/')
@route('/welcome')
@route('/index.html')
def welcome():
    return template('welcome.tpl')
