from bottle import route, template, request, redirect
from models.consulate import Consulate


@route('/consulates/new')
def new_form():
    return template('consulate_new_form.tpl')


@route('/consulates/new', method='POST')
def new_results():
    try:
        consulate_params = {}

        consulate_params['name'] = request.forms.get('name')
        consulate_params['postal_code'] = request.forms.get('postal_code')
        consulate_params['neighborhood'] = request.forms.get('neighborhood')
        consulate_params['district'] = request.forms.get('district')
        consulate_params['latitude'] = request.forms.get('latitude')
        consulate_params['longitude'] = request.forms.get('longitude')

        new_consulate = Consulate.new(consulate_params)
        message = "Item was successfully created!"
    except Exception, ValueError:
        message = "An error occurred while performing the requested action"
    finally:
        return template('operation_result.tpl', message=message)


@route('/consulates/delete')
def delete_form():
    return template('consulate_delete_form.tpl')


@route('/consulates/delete', method='POST')
def delete_results():
    try:
        consulate_id = request.forms.get('id')

        consulates = Consulate.find('id', consulate_id)
        consulates[0].destroy()

        message = "Item was successfully deleted!"
    except:
        message = "An error occurred while performing the requested action"
    finally:
        return template('operation_result.tpl', message=message)


@route('/consulates/filter')
def filter_form():
    return template('consulate_filter_form.tpl')


@route('/consulates/filter', method='POST')
def filter_results():
    try:
        filter_name = request.forms.get('field_name')
        filter_value = request.forms.get('field_value')
        consulates = Consulate.find(filter_name, filter_value)
        return template('consulate_filter_results.tpl', consulates=consulates)
    except:
        message = "An error occurred while performing the requested action"
        return template('operation_result.tpl', message=message)


@route('/consulates')
def all():
    try:
        consulates = Consulate.all()
        return template('consulate_all.tpl', data=consulates)
    except:
        message = "An error occurred while performing the requested action"
        return template('operation_result.tpl', message=message)
