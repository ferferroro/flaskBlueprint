from flask import Blueprint, render_template, redirect, url_for
from main.models.contactusModelClass import ContactUs

# instantiate blue print 
contactus_route = Blueprint('contactus', __name__)

# ContactUs route - show all
@contactus_route.route('/contact_us', methods=['GET'])
def contacts():
    # ---- This is my change | Now this 'contact us' route will always load the homepage
    # ---- Key thing to look at this is 'index.index' | this might look redundant but its not
    # ---- Try opening the indexRoute.py - and we have this code   ===>>> 'index_route = Blueprint('index', __name__)'
    # ---- we have instantiated or named the blue print as 'index'
    # ---- then open again the indexRoute.py and we have this code ===>>> 'def index():'
    # ---- the name of the function is 'index'
    # ---- so if you are using url_for in a blueprint - please consider checking 'Name of Blueprint . Name of Function'
    return redirect(url_for('index.index')) 

    # ---- This is the old code that calls the contact us page
    # contacts = ContactUs.query.all()
    # return render_template('contact_us.html', contacts=contacts)