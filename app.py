import os
import jsonify
from flask import request, render_template
from db import Mdb
import traceback
from eve import Eve

#app = Flask(__name__)
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Eve('Karma-App', template_folder=tmpl_dir)

mdb = Mdb()

@app.route('/')
def main_page():
    templateData = {'title': 'Signup Page'}
    return render_template('company/index.html', **templateData)


#############################################
#                                           #
#              REGISTER COMPANY             #
#                                           #
#############################################
"""
@app.route("/company/signup", methods=['POST'])
def add_user():
    try:
        name = request.form['name']
        registration = request.form['regis']
        city = request.form['city']
        state = request.form['state']
        zip = request.form['zip']
        country = request.form['country']
        company = request.form['company']
        phone = request.form['phone']
        mobile = request.form['mobile']
        email = request.form['email']
        password = request.form['password']
        website = request.form['website']

        mdb.add_user(name, registration, city, state, zip, country, company,
                     phone, email, password, website)
        print('User is added successfully')
        templateData = {'title': 'Signin Page'}
        return render_template('company/signin.html', **templateData)
    except Exception as exp:
        print('add_user() :: Got exception: %s' % exp)
        print(traceback.format_exc())
"""


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


#############################################
#                                           #
#                 LOGIN USER                #
#                                           #
#############################################
@app.route('/login', methods=['POST'])
def login():

    try:
        email = request.form['email']
        password = request.form['password']
        if mdb.company_exists(email, password):
            print 'Login Successfully'
            templateData = {'title': 'singin page'}
        else:
            return render_template('/company/index.html', **templateData)
    except Exception as exp:
        print 'login() :: Got exception: %s' % exp
        print(traceback.format_exc())
    templateData = {'title': 'singin page'}
    return render_template('/company/save.html', **templateData)


#############################################
#                                           #
#                  MAIN SERVER              #
#                                           #
#############################################
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True, threaded=True)
