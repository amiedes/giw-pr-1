from bottle import route, template, request, redirect
from models.consulate import Consulate
from lib.authentication import Authentication, AuthenticationException

@route('/consulates/new')
def new_form():
    try:
        Authentication.check_session
        return template('consulate_new_form.tpl')
    except AuthenticationException as ae:
        message = "You are not logged in!"
        return template('operation_result.tpl', message=message)


@route('/consulates/new', method='POST')
def new_results():
    try:
        Authentication.check_session

        consulate_params = {}

        consulate_params['name'] = request.forms.get('name')
        consulate_params['postal_code'] = request.forms.get('postal_code')
        consulate_params['neighborhood'] = request.forms.get('neighborhood')
        consulate_params['district'] = request.forms.get('district')
        consulate_params['latitude'] = request.forms.get('latitude')
        consulate_params['longitude'] = request.forms.get('longitude')

        new_consulate = Consulate.new(consulate_params)
        message = "Item was successfully created!"
    except AuthenticationException as ae:
        message = "You are not logged in!"
    except:
        message = "An error occurred while performing the requested action"
    finally:
        return template('operation_result.tpl', message=message)


@route('/consulates/delete')
def delete_form():
    try:
        Authentication.check_session
        return template('consulate_delete_form.tpl')
    except AuthenticationException as ae:
        message = "You are not logged in!"
        return template('operation_result.tpl', message=message)
    return template('consulate_delete_form.tpl')


@route('/consulates/delete', method='POST')
def delete_results():
    try:
        Authentication.check_session

        if (request.forms.get('id')):
            consulate_id = request.forms.get('id')

            consulates = Consulate.find('id', consulate_id)
            consulates[0].destroy()

            message = "Item was successfully deleted!"
        else:
            message = "You must eneter the id!"
    except AuthenticationException as ae:
        message = "You are not logged in!"
    except:
        message = "An error occurred while performing the requested action"
    finally:
        return template('operation_result.tpl', message=message)


@route('/consulates/filter')
def filter_form():
    try:
        Authentication.check_session
        return template('consulate_filter_form.tpl')
    except AuthenticationException as ae:
        message = "You are not logged in!"
        return template('operation_result.tpl', message=message)


@route('/consulates/filter', method='POST')
def filter_results():
    try:
        Authentication.check_session

        filter_name = request.forms.get('field_name')
        filter_value = request.forms.get('field_value')
        consulates = Consulate.find(filter_name, filter_value)
        return template('consulate_filter_results.tpl', consulates=consulates)
    except AuthenticationException as ae:
        message = "You are not logged in!"
    except:
        message = "An error occurred while performing the requested action"
    finally:
        return template('operation_result.tpl', message=message)


@route('/consulates/modify')
def modify_form():
    try:
        Authentication.check_session
        return template('consulate_update.tpl')
    except AuthenticationException as ae:
        message = "You are not logged in!"
        return template('operation_result.tpl', message=message)


@route('/consulates/modify', method='POST')
def modify_results():
    try:
        Authentication.check_session

        consulate_params = {}

        if (request.forms.get('name')):
            consulate_params['name'] = request.forms.get('name')
        if (request.forms.get('postal_code')):
            consulate_params['postal_code'] = request.forms.get('postal_code')
        if (request.forms.get('neighborhood')):
            consulate_params['neighborhood'] = request.forms.get('neighborhood')
        if (request.forms.get('district')):
            consulate_params['district'] = request.forms.get('district')
        if (request.forms.get('latitude')):
            consulate_params['latitude'] = request.forms.get('latitude')
        if (request.forms.get('longitude')):
            consulate_params['longitude'] = request.forms.get('longitude')

        if (request.forms.get('id')):
            requested_id = request.forms.get('id')
            consulates = Consulate.find('id', requested_id)
            consulates[0].modify(consulate_params, requested_id)
            message = "Item was successfully modified!"
        else:
            message = "You must enter the id!"
    except AuthenticationException as ae:
        message = "You are not logged in!"
    except:
        message = "An error occurred while performing the requested action"+ str(consulate_params)
    finally:
        return template('operation_result.tpl', message=message)


@route('/consulates')
def all():
    try:
        Authentication.check_session

        consulates = Consulate.all()
        return template('consulate_all.tpl', data=consulates)
    except AuthenticationException as ae:
        message = "You are not logged in!"
    except:
        message = "An error occurred while performing the requested action"
    finally:
        return template('operation_result.tpl', message=message)
