from flask import Blueprint, render_template
from main.models.servicesModelClass import Services

# instantiate blue print 
services_route = Blueprint('services', __name__)

# Services route - show all
@services_route.route('/services', methods=['GET'])
def services():
    services = Services.query.all()
    return render_template('services.html', services=services)

# Services route - view 
@services_route.route('/service/<id>', methods=['GET'])
def service_view(id):
    service = Services.query.filter_by(id=id).first()
    return render_template('view_service.html', service=service)