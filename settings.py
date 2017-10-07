import os

# we want to seamlessy run our API both locally and on Heroku.
# If running on Heroku, sensible DB connection settings are
# stored in environment variables.
MONGO_HOST = os.environ.get('MONGO_HOST', 'ds113505.mlab.com')
MONGO_PORT = os.environ.get('MONGO_PORT', 13505)
MONGO_USERNAME = os.environ.get\
    ('MONGO_USERNAME', 'karmadbuser1') # FIXME set username later
MONGO_PASSWORD = os.environ.get\
    ('MONGO_PASSWORD', 'karmadbuser1') # FIXME set password later
MONGO_DBNAME = os.environ.get\
    ('MONGO_DBNAME', 'karma')

# MONGO_AUTH_SOURCE = os.environ.get\
#    ('MONGO_AUTH_SOURCE', 'admin')


RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

URL_PREFIX="api"

#########################################
#              Company Schema           #
#########################################
company = {

    # 'title' tag used in item links.
    'item_title': 'company',

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.

    'schema': {

        '_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },

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

    }
}


#########################################
#             Manager Schema            #
#########################################
manager = {
    'item_title': 'manager',

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.

    'schema': {

        '_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },

        'company_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },

        'user_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },
    }

}


#########################################
#               User Schema             #
#########################################
user = {
    'item_title': 'user',

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.

    'schema': {

        '_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },

        'f_name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },

        'l_name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },

        'email': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },

        'password': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },
    }
}


#########################################
#             Project Schema            #
#########################################
project = {
    'item_title': 'project',

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.

    'schema': {

        '_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },

        'manager_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },

        'title': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },

        'start_date': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },

        'end_date': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },

        'description': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },
    }

}


#########################################
#             Worker Schema             #
#########################################
worker = {
    'item_title': 'worker',

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.

    'schema': {

        '_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },

        'project_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },

        'user_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },
    }

}


#########################################
#               Task Schema             #
#########################################
task = {
    'item_title': 'task',

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.

    'schema': {

        '_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },

        'project_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },

        'worker_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },
    }

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
