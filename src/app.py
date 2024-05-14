from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

# instance of SQLAlchemy
db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'PamantasanPH'
    # configuring the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # configuring the mail
    app.config['MAIL_SERVER'] ='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = '@gmail.com'
    app.config['MAIL_PASSWORD'] = ''
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USE_TLS'] = True

    # initializing the database and mail
    db.init_app(app)
    mail.init_app(app)

    with app.app_context():
        db.create_all()

    return app