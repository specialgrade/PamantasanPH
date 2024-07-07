from datetime import datetime
from src.app import db, login_manager, bcrypt
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer  as Serializer
from flask import current_app as app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# this is the model for subscription to the newsletter=============================================
class Subscribe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Subscribe {self.email}>'

# this is the model for user register-login-logout=================================================
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(128), nullable=False)

    ratings = db.relationship('Rating', backref='user', lazy=True)
    todos = db.relationship('Todo', backref='user', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')
    
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
            return User.query.get(user_id)
        except:
            return None
        
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

# this is the model for university reviews=========================================================
class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    university_id = db.Column(db.Integer, db.ForeignKey('university.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
        
    def __repr__(self):
        return f'<Rating {self.rating} for University {self.university_id} by User {self.user_id}>'
        
class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(255))

    ratings = db.relationship('Rating', backref='university', lazy=True)

    def __repr__(self):
        return '<University %r>' % self.name

# this is the model for user's todo list==========================================================
class Todo(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100))
    status = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Todo {self.task} for User {self.user_id}>'