import os

# we want to seamlessy run our API both locally and on Heroku.
# If running on Heroku, sensible DB connection settings are
# stored in environment variables.
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'admin') #FIXME set username later
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', '123') #FIXME set password later
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'karma')

MONGO_AUTH_SOURCE = os.environ.get('MONGO_AUTH_SOURCE', 'admin')


RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

company = {

    # 'title' tag used in item links.
    'item_title': 'company',

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.

    'schema': {

        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },

        'email': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
            'required': True,
            # talk about hard constraints! For the purpose of the demo
            # 'lastname' is an API entry-point, so we need it to be unique.
            'unique': True,
        },

        'password': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
            'required': True,
        },

        'mobile': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
            'required': True,
            'unique': True,
        },

        'tel_no': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
        },

        'address_line1': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
            'unique': True,
        },

        'address_line2': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
        },

        'registration_no': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
        },

        'city': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
            'unique': True,
        },

        'country': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
        },

        'zip': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
        },

        'website': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
        },





        # 'role' is a list, and can only contain values from 'allowed'.
        'role': {
            'type': 'list',
            'allowed': ["author", "contributor", "copy"],
        },
        # An embedded 'strongly-typed' dictionary.
        'location': {
            'type': 'dict',
            'schema': {
                'address': {'type': 'string'},
                'city': {'type': 'string'}
            },
        },
        'born': {
            'type': 'datetime',
        },
    }
}

"""
manager
->  _id
->  company_id
->  user_id

user
->  _id
->  f_name
->  l_name
->  email
->  password


project
->  _id
->  manager_id
->  title
->  start_date
->  end_date
->  description


worker
->  _id
->  project_id
->  user_id


task
->  _id
->  project_id
->  worker_id



"""
manager = {

}


user = {

}

project = {

}

worker = {

}

task = {

}


# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'company': company,
    'manager': manager,
    'user': user,
    'project': project,
    'worker': worker,
    'task': task,

}


# quick check current settings
if __name__ == "__main__":
    print ("Current settings are")
    print ("MONGO_HOST: %s" % MONGO_HOST)
