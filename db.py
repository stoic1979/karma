from pymongo import MongoClient
from flask import jsonify
import traceback
import json
import datetime
from bson import ObjectId


class Mdb:

    def __init__(self):
        conn_str = "mongodb://karmadbuser1:" \
                    "karmadbuser1@ds113505.mlab.com:13505/karma"

        client = MongoClient(conn_str)
        self.db = client['karma']

#############################################
#                                           #
#                   ADD COMPANY             #
#                                           #
#############################################
    def add_company(self, name, registration, city, state, zip, country,
                    company, phone, email, pw_hash, website):
        try:

            rec = {
                'name': name,
                'registration': registration,
                'city': city,
                'state': state,
                'zip': zip,
                'country': country,
                'company': company,
                'phone': phone,
                'email': email,
                'password': pw_hash,
                'website': website
            }

            self.db.company.insert(rec)

        except Exception as exp:
            print "add_user() :: Got exception: %s", exp
            print(traceback.format_exc())

#############################################
#                                           #
#           CHECK USER IN DATABASE          #
#                                           #
#############################################
    def company_exists(self, email):
        """
        function checks if a user with given email and password
        exists in database
        :param email: email of the user
        :param password: password of the user
        :return: True, if user exists,
                 False, otherwise
        """
        return self.db.company.find({'email': email}).count() > 0

    def admin_exists(self, email, password):

        return self.db.admin.find({'email': email, 'password': password}).\
                   count() > 0

#############################################
#                                           #
#                   GET PASSWORD            #
#                                           #
#############################################
    def get_password(self, email):
        result = self.db.company.find({'email': email})
        name = ''
        password = ''
        if result:
            for data in result:
                name = data['name']
                password = data['password']
                print 'password in db class', password
        return password

#############################################
#                                           #
#        GET NAME ACCORDING TO EMAIL        #
#                                           #
#############################################
    def get_name(self, email):
        result = self.db.company.find({'email': email})
        name = ''
        email = ''
        if result:
            for data in result:
                name = data['name']
                email = data['email']
        return name

#############################################
#                                           #
#            USER SESSION IN DATABASE       #
#                                           #
#############################################
    # def save_login_info(self, user_email, mac, ip, user_agent, type):
    #     LOGIN_TYPE = 'company Login'
    #     try:
    #         ts = datetime.datetime.today().strftime("%a %b %d %X  %Y ")
    #
    #         rec = {
    #             'user_id': user_email,
    #             'mac': mac,
    #             'ip': ip,
    #             'user_agent': user_agent,
    #             'user_type': type,
    #             'timestamp': ts
    #         }
    #
    #         self.db.company_session.insert(rec)
    #     except Exception as exp:
    #         print "save_login_info() :: Got exception: %s", exp
    #         print(traceback.format_exc())

    def get_sessions(self):
        collection = self.db["user_session"]
        result = collection.find({})
        ret = []
        for data in result:
            ret.append(data)
        return ret

if __name__ == '__main__':
    mdb = Mdb()
