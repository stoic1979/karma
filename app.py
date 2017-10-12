import os
from flask import request, render_template, session, url_for, redirect


from db import Mdb
import traceback
import time
import jwt
import datetime
from datetime import datetime, timedelta
import json
from werkzeug.utils import secure_filename
from flask.ext.bcrypt import Bcrypt
from eve import Eve
from flask_login import LoginManager, UserMixin, login_user, login_required,\
                        logout_user, current_user

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'templates')
app = Eve('Karma-App', template_folder=tmpl_dir)
bcrypt = Bcrypt(app)

mdb = Mdb()

app.config['secretkey'] = 'some-strong+secret#key'
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'

# setup login manager
login_manager = LoginManager()
login_manager.init_app(app)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


#############################################
#                                           #
#                SESSION COUNTER            #
#                                           #
#############################################
def sumSessionCounter():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1


@app.route('/')
def main_page():
    templateData = {'title': 'Signup Page'}
    return render_template('company/index.html', **templateData)


#############################################
#                                           #
#              TOKEN REQUIRED               #
#                                           #
#############################################
app.config['secretkey'] = 'some-strong+secret#key'


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        # ensure that token is specified in the request
        if not token:
            return jsonify({'message': 'Missing token!'})

        # ensure that token is valid
        try:
            data = jwt.decode(token, app.config['secretkey'])
        except:
            return jsonify({'message': 'Invalid token!'})

        return f(*args, **kwargs)

    return decorated


#############################################
#                                           #
#              REGISTER COMPANY             #
#                                           #
#############################################
@app.route("/company/signup", methods=['POST'])
def add_company():
    try:
        name = json_data['name']
        registration = json_data['regis']
        city = json_data['city']
        zip = json_data['zip']
        country = json_data['country']
        phone = json_data['phone']
        mobile = json_data['mobile']
        email = json_data['email']
        password = json_data['password']
        website = json_data['website']


        # password bcrypt  #
        pw_hash = bcrypt.generate_password_hash(password)
        passw = bcrypt.check_password_hash(pw_hash, password)

        mdb.add_company(name, registration, city, zip, country,
                     phone, email, pw_hash, website)
        print('Company is added successfully')
        templateData = {'title': 'Signin Page'}
        return render_template('company/signin.html', **templateData)
    except Exception as exp:
        print('add_company() :: Got exception: %s' % exp)
        print(traceback.format_exc())

'''
@app.route("/company/signup", methods=['POST'])
def add_user():
    try:
        json_data = request.json['info']
        print "=====================", json_data
        name = json_data['name']
        registration = json_data['regis']
        city = json_data['city']
        zip = json_data['zip']
        country = json_data['country']
        phone = json_data['phone']
        mobile = json_data['mobile']
        email = json_data['email']
        password = json_data['password']
        website = json_data['website']

        mdb.add_user(name, registration, city, zip, country,
                     phone, email, password, website)
        print('User is added successfully')
        templateData = {'title': 'Signin Page'}
        return render_template('company/signin.html', **templateData)
    except Exception as exp:
        print('add_user() :: Got exception: %s' % exp)
        print(traceback.format_exc())
        return "Not done"
'''

@app.route('/company', methods=['GET'])
def company():
    templateData = {'title': 'Home Page'}
    return render_template('company/index.html', **templateData)


@app.route('/company/signup')
def signup():
    templateData = {'title': 'signup Page'}
    return render_template('company/signup.html', **templateData)


@app.route('/company/signin')
def signin():
    templateData = {'title': 'Signin Page'}
    return render_template('company/signin.html', **templateData)


@app.route('/company/projects')
def projects():
    templateData = {'title': 'projects Page'}
    return render_template('company/projects.html', **templateData)


#############################################
#                                           #
#                LOGIN COMPANY              #
#                                           #
#############################################
@app.route('/login', methods=['POST'])
def login():
    ret = {'err': 0}
    try:
        sumSessionCounter()
        email = request.form['email']
        password = request.form['password']

        if mdb.company_exists(email):
            pw_hash = mdb.get_password(email)
            print 'password in server, get from db class', pw_hash
            passw = bcrypt.check_password_hash(pw_hash, password)

            if passw == True:
                name = mdb.get_name(email)
                session['name'] = name
                session['email'] = email

                # Login Successful!
                expiry = datetime.datetime.utcnow() + datetime.\
                    timedelta(minutes=30)
                token = jwt.encode({'user': email, 'exp': expiry},
                                   app.config['secretkey'], algorithm='HS256')

                ret['msg'] = 'Login successful'
                ret['err'] = 0
                ret['token'] = token.decode('UTF-8')
                templateData = {'title': 'singin page'}
            else:
                return render_template('/company/save.html', session=session)

        else:
            # Login Failed!
            return render_template('/company/save.html', session=session)

    except Exception as exp:
        ret['msg'] = '%s' % exp
        ret['err'] = 1
        print(traceback.format_exc())
    # return jsonify(ret)
    return render_template('/company/save.html', session=session)


#############################################
#              SESSION LOGOUT               #
#############################################
@app.route('/clear')
def clearsession():
    session.clear()
    return render_template('/company/index.html', session=session)


@app.route('/user')
def user():
    templateData = {'title': 'home Page'}
    return render_template('/user/index.html', **templateData)


@app.route('/user/signup')
def user_signup():
    templateData = {'title': 'signup Page'}
    return render_template('/user/signup.html', **templateData)


@app.route('/user/signin')
def user_signin():
    templateData = {'title': 'Signin Page'}
    return render_template('/user/signin.html', **templateData)


@app.route('/user/task')
def user_task():
    templateData = {'title': 'Task Page'}
    return render_template('/user/task.html', **templateData)


@app.route('/user/worker')
def user_worker():
    templateData = {'title': 'worker Page'}
    return render_template('/user/worker.html', **templateData)


@app.route('/user/manager')
def user_manager():
    templateData = {'title': 'manager Page'}
    return render_template('/user/manager.html', **templateData)


@app.route('/user/project')
def user_project():
    templateData = {'title': 'project Page'}
    return render_template('/user/project.html', **templateData)


#############################################
#                                           #
#                  MAIN SERVER              #
#                                           #
#############################################
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True, threaded=True)
