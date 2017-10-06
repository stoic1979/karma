from flask import Flask, request, render_template
from db import Mdb
import traceback

app = Flask(__name__)
mdb = Mdb()


@app.route('/')
def home():
    templateData = {'title': 'Signup Page'}
    return render_template('company/index.html', **templateData)


#############################################
#                                           #
#              REGISTER COMPANY             #
#                                           #
#############################################
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
    except Exception as exp:
        print('add_user() :: Got exception: %s' % exp)
        print(traceback.format_exc())
    return render_template('company/signin.html', **templateData)


@app.route('/company')
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
    app.run(debug=True)
