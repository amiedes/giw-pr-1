from bottle import route, template, request
from models.consulate import Consulate


@route('/consulates/filter')
def filter_form():
    return template('consulates_filter_form.tpl')


@route('/consulates/filter', method='POST')
def filter_results():
    filter_name = request.forms.get('field_name')
    filter_value = request.forms.get('field_value')
    consulates = Consulate.find(filter_name, filter_value)
    return template('filtered_consulates.tpl', consulates=consulates)


@route('/consulates')
def all():
    consulates = Consulate.all()
    return template('all_consulates.tpl', data=consulates)
