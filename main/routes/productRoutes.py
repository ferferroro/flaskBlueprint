from flask import Blueprint, render_template
from main.models.productModelClass import Product

# instantiate blue print 
product_route = Blueprint('product', __name__)

# Product route - show all
@product_route.route('/', methods=['GET'])
def product():
    products = Product.query.all()
    return render_template('products.html', products=products)

# Product route - view
@product_route.route('/<id>', methods=['GET'])
def product_view(id):
    product = Product.query.filter_by(id=id).first()
    return render_template('view_product.html', product=product)