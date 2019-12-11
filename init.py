from app import db, Product, Services, ContactUs

db.create_all()

new_prod = Product(code='PROD100', name='This is a product name 1', quantity=1)
db.session.add(new_prod)
db.session.commit()

new_prod = Product(code='PROD200', name='This is a product name 2', quantity=2)
db.session.add(new_prod)
db.session.commit()

new_prod = Product(code='PROD300', name='This is a product name 3', quantity=3)
db.session.add(new_prod)
db.session.commit()

new_serv = Services(code='SERV100', name='This is a service name 1', price=100)
db.session.add(new_serv)
db.session.commit()

new_serv = Services(code='SERV200', name='This is a service name 2', price=200)
db.session.add(new_serv)
db.session.commit()

new_serv = Services(code='SERV300', name='This is a service name 3', price=300)
db.session.add(new_serv)
db.session.commit()

new_contact = ContactUs(key='email address', value='email1@email.com')
db.session.add(new_contact)
db.session.commit()

new_contact = ContactUs(key='Phone', value='1234576')
db.session.add(new_contact)
db.session.commit()