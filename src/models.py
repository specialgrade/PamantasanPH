from .app import db
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# create subscribe class that inherits from db.model
class Subscribe(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), unique=True, nullable = False)

    def __repr__(self):
        return '<Subscriber %r>' % self.email
    
