from main import db

# Product model class
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(15))
    name = db.Column(db.String(50))
    quantity = db.Column(db.Integer)