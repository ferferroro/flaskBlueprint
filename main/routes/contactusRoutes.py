from flask import Blueprint, render_template
from main.models.contactusModelClass import ContactUs

# instantiate blue print 
contactus_route = Blueprint('contactus', __name__)

# ContactUs route - show all
@contactus_route.route('/contact_us', methods=['GET'])
def contacts():
    contacts = ContactUs.query.all()
    return render_template('contact_us.html', contacts=contacts)