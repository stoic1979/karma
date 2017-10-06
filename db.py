from pymongo import MongoClient
import traceback


class Mdb:

    def __init__(self):
        conn_str = "mongodb://admin:123@127.0.0.1:27017/admin"
        client = MongoClient(conn_str)
        self.db = client['karma']

    def add_user(self, name, registration, city, state, zip, country, company,
                 phone, email, password, website):
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
                'password': password,
                'website': website
            }

            self.db.company.insert(rec)

        except Exception as exp:
            print "add_user() :: Got exception: %s", exp
            print(traceback.format_exc())

    def company_exists(self, email, password):
        """
        fucntion check if a user given email and password
        exists in database
        :return:
        """
        return self.db.company.find({'email': email, 'password': password})\
                   .count() > 0

if __name__ == '__main__':
    mdb = Mdb()
