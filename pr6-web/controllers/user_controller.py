from bottle import route, template, get, static_file, request
from models.user import User

@route('/')
@route('/index.html')
@route('/login')
def login():
    return template('login.tpl')

@route ('/login', method='POST')
def do_login():
    try:        
        username = request.forms.get('username')
        #password = request.forms.get('password')
        user = User.find('username', username)
        
        message = "You have logged in successfully as " + user + "!"
    except:
        message = "An error occurred while performing the requested action"
    finally:
        return template('successful_login.tpl', message=message)

@route ('/register', method='POST')
def do_register():
    try:
        user_params = {}
        user_params['username'] = request.forms.get('new_username')
        user_params['password'] = request.forms.get('new_password')
        user_params['name'] = request.forms.get('name')
        user_params['surname'] = request.forms.get('surname')
        
        new_user = User.new(user_params)
        message = "Account was created correctly"
    except:
        message = "An error occurred while performing the requested action"
    
        
