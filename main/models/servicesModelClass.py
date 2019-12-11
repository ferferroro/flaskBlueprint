from main import db

# Services model class
class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(15))
    name = db.Column(db.String(50))
    price = db.Column(db.Float)