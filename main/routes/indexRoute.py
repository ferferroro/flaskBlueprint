from flask import Blueprint, render_template

# instantiate blue print 
index_route = Blueprint('index', __name__)

# define route
@index_route.route('/')
def index():
    return render_template('index.html')