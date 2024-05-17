from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

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

    EMAIL = os.getenv('email')
    PASSWORD = os.getenv('password')

    app.config['MAIL_SERVER'] ='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = EMAIL
    app.config['MAIL_PASSWORD'] = PASSWORD
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USE_TLS'] = False

    # initializing the database and mail
    db.init_app(app)
    mail.init_app(app)

    with app.app_context():
        db.create_all()

    return app