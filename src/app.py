from flask import Flask, request 
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import os 

db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config['SECRET_KEY'] = "PamantasanPH"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config ['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config ['MAIL_PORT'] = 465
    app.config ['MAIL_USERNAME'] = 'pamantasanph@gmail.com'
    app.config ['MAIL_PASSWORD'] = 'PamantasanPH2024'
    app.config ['MAIL_USE_TLS'] = False
    app.config ['MAIL_USE_SSL'] = True

    db.init_app(app)
    mail.init_app(app)

    with app.app_context():
        db.create_all()

    return app