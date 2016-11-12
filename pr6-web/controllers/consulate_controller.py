from bottle import route, template
from models.consulate import Consulate


@route('/consulate/<id>')
def show():
    return 'TODO: a single item based on id'


@route('/consulates')
def index():
    consulates = Consulate.all()
    return template('all_consulates.tpl', data=consulates)
