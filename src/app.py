from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail, Message
from authlib.integrations.flask_client import OAuth
import os
from dotenv import load_dotenv

load_dotenv()

# Instance of SQLAlchemy
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
mail = Mail()
oauth = OAuth()

def create_app():
    app = Flask(__name__, template_folder='templates')

    # Load configurations from .env file
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Mail configuration
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    oauth.init_app(app)

    login_manager.login_view = 'login'
    login_manager.login_message_category = 'info'

    # OAuth registration
    google = oauth.register(
        name='google',
        client_id=os.getenv('GOOGLE_CLIENT_ID'),
        client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
        server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
        client_kwargs={'scope': 'openid profile email'}
    )

    facebook = oauth.register(
        name='facebook',
        client_id=os.getenv('FACEBOOK_APP_ID'),
        client_secret=os.getenv('FACEBOOK_APP_SECRET'),
        authorize_url='https://www.facebook.com/dialog/oauth',
        access_token_url='https://graph.facebook.com/oauth/access_token',
        client_kwargs={'scope': 'email'}
    )

    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    return app
