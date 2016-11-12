from bottle import route, template
from models.consulate import Consulate


@route('/consulates/<filter_name>/<filter_value>')
def filter(filter_name, filter_value):
    consulates = Consulate.find(filter_name, filter_value)
    return template('filtered_consulates.tpl', consulates=consulates)


@route('/consulates')
def all():
    consulates = Consulate.all()
    return template('all_consulates.tpl', data=consulates)
