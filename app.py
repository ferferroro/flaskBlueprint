from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# instantiate the app
app =  Flask(__name__)

# configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample_db.sqlite'

# instantiate database
db = SQLAlchemy(app)

# Product model class
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(15))
    name = db.Column(db.String(50))
    quantity = db.Column(db.Integer)

# Services model class
class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(15))
    name = db.Column(db.String(50))
    price = db.Column(db.Float)

# ContactUs model class
class ContactUs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50))
    value = db.Column(db.String(50))

# index route
@app.route('/')
def index():
    return render_template('index.html')

# Product route - show all
@app.route('/product', methods=['GET'])
def product():
    products = Product.query.all()
    return render_template('products.html', products=products)

# Product route - view
@app.route('/product/<id>', methods=['GET'])
def product_view(id):
    product = Product.query.filter_by(id=id).first()
    return render_template('view_product.html', product=product)


# Services route - show all
@app.route('/services', methods=['GET'])
def services():
    services = Services.query.all()
    return render_template('services.html', services=services)

# Services route - view 
@app.route('/service/<id>', methods=['GET'])
def service_view(id):
    service = Services.query.filter_by(id=id).first()
    return render_template('view_service.html', service=service)

# ContactUs route - show all
@app.route('/contact_us', methods=['GET'])
def contacts():
    contacts = ContactUs.query.all()
    return render_template('contact_us.html', contacts=contacts)

if __name__ == '__main__':
    app.run(debug=True)
