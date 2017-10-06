////////////////////////////////
//          Company           //
////////////////////////////////
c1 = {
    'name': 'Weavebytes',
    'email': 'bytes@gmail.com',
    'password':'123',
    'mobile': '123456',
    'tel_no': '0197812345',
    'address_line1':'city',
    'address_line2': 'kharar',
    'registration_no':'2019238',
    'city': 'punjab',
    'country':'India',
    'zip':'12098',
    'website':'www.bytes.com',
    },
db.company.insert(c1);

c2 = {
    'name': 'My Construction Company',
    'email': 'minerva@gmail.com',
    'password':'123',
    'mobile': '123456',
    'tel_no': '0197812345',
    'address_line1':'gmw',
    'address_line2': 'bilaspur',
    'registration_no':'2019238',
    'city': 'punjab',
    'country':'India',
    'zip':'12098',
    'website':'www.city.com'
    },
db.company.insert(c2);

c3 = {
    'name': 'vodafone',
    'email': 'vodafone@gmail.com',
    'password':'123',
    'mobile': '123456',
    'tel_no': '0197812345',
    'address_line1':'gmw',
    'address_line2': 'chandigarh',
    'registration_no':'2019238',
    'city': 'punjab',
    'country':'India',
    'zip':'12098',
    'website':'www.vodafone.com'
    },
db.company.insert(c3);


////////////////////////////////
//          manager           //
////////////////////////////////
m1 = {
    'company_id': '',
    'user_id': 'tom@gmail.com'
    }
db.manager.insert(m1)

m2 = {
    'company_id': '',
    'user_id': 'tommy@gmail.com'
    }
db.manager.insert(m2)

m3 = {
    'company_id': '',
    'user_id': 'jon@gmail.com'
    }
db.manager.insert(m3)


////////////////////////////////
//          user              //
////////////////////////////////
u1 = {
    'f_name': 'tom',
    'l_name': 'jerry',
    'email': 'tom@gmail.com',
    'password': '123'
    }
db.user.insert(u1)

u2 = {
    'f_name': 'tommy',
    'l_name': 'jerry',
    'email': 'tommy@gmail.com',
    'password': '123'
    }
db.user.insert(u2)


u3 = {
    'f_name': 'jon',
    'l_name': 'jerry',
    'email': 'jon@gmail.com',
    'password': '123'
    }
db.user.insert(u3)


////////////////////////////////
//          project           //
////////////////////////////////
p1 = {
    'manager_id': '123',
    'title': 'karma',
    'start_date': '8/10/2017',
    'end_date': '12/12/2017'
    'description': 'python, mongo, flask'
    }
db.project.insert(p1)

p2 = {
    'manager_id': '124',
    'title': 'projact manager',
    'start_date': '18/10/2017',
    'end_date': '12/01/2018'
    'description': 'python, mongo, flask'
    }
db.project.insert(p2)

p3 = {
    'manager_id': '125',
    'title': 'kirk',
    'start_date': '8/10/2017',
    'end_date': '12/12/2017'
    'description': 'python, mongo, flask'
    }
db.project.insert(p3)


////////////////////////////////
//          worker            //
////////////////////////////////
w1 = {
    'project_id': '1',
    'user_id': 'karma'
    }
db.worker.insert(w1)

w2 = {
    'project_id': '2',
    'user_id': 'project manager'
    }
db.worker.insert(w2)

w3 = {
    'project_id': '1',
    'user_id': 'kirk'
    }
db.worker.insert(w3)


////////////////////////////////
//          task              //
////////////////////////////////
t1 = {
    'project_id': '1',
    'worker_id': 'kirk'
    }
db.task.insert(t1)

t2 = {
    'project_id': '1',
    'worker_id': 'karma'
    }
db.task.insert(t2)

t3 = {
    'project_id': '1',
    'worker_id': 'kirk'
    }
db.task.insert(t3)
