from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# instantiate the app
app =  Flask(__name__)

# configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample_db.sqlite'

# instantiate database
db = SQLAlchemy(app)

# import routes
from main.routes.indexRoute import index_route
from main.routes.productRoutes import product_route
from main.routes.servicesRoutes import services_route
from main.routes.contactusRoutes import contactus_route

# register blueprint
app.register_blueprint(index_route)
app.register_blueprint(product_route, url_prefix='/product')
app.register_blueprint(services_route)
app.register_blueprint(contactus_route)