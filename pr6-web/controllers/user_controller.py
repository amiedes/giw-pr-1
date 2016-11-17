from bottle import route, template, get, static_file, request, response
from models.user import User
from lib.authentication import Authentication

@route('/')
@route('/index.html')
@route('/login')
def login():
    return template('login.tpl')

@route ('/login', method='POST')
def do_login():
    try:
        print "TRYINT TO DO LOGIN"
        username = request.forms.get('username')
        password = request.forms.get('password')

        print "NOW I'LL CHECK LOGIN"
        user_id = Authentication.check_login(username, password)

        if user_id >= 0:
            print "NOW I'LL CREATE A SESSION"
            #Authentication.create_session(request, user_id)
            print "User ID: ", user_id
            response.set_cookie("session_id", str(user_id))
            print "response cookie set correctly"
            message = "Login was successful!"
        else:
            message = "Your login data was not correct"
    except:
        message = "An error occurred while performing the requested action"
    finally:
        return template('successful_login.tpl', message=message)

@route ('/register', method='POST')
def do_register():
    try:
        user_params = {}
        user_params['name'] = request.forms.get('name')
        user_params['surname'] = request.forms.get('surname')
        user_params['username'] = request.forms.get('new_username')
        user_params['password'] = request.forms.get('new_password')
        User.new(user_params)
        message = "Account was created correctly"
    except:
        message = "An error occurred while performing the requested action"
    finally:
        return template('login.tpl', message=message)
