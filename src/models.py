from .app import db

# create subscribe class that inherits from db.model
class Subscribe(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), nullable = False)

    def __repr__(self):
        return '<Subscriber %r>' % self.email