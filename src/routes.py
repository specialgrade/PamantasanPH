from flask import render_template, redirect, url_for, request, flash
from .app import db, mail
from .models import Subscribe
from flask import send_from_directory
from flask_mail import Mail, Message
from sqlalchemy.exc import SQLAlchemyError

def init_app(app):
    
    # routes to go to the home page
    @app.route('/', methods=['GET', 'POST'])
    def index():
        return render_template('index.html')
    
    # when users click the home button, they will be redirected to the home page
    @app.route('/home', methods=['GET', 'POST'])
    def home():
        return render_template('index.html')
    
    # routes to render the univs.html when they click the Universities button from the home page
    @app.route('/home/universities', methods=['GET'])
    def universities():
        return render_template('univs.html')
    
    # route for sending email to the users
    @app.route('/newsletter', methods=['POST'])
    def newsletter():
        try:
            recipient = request.form.get('email')
            new_recipient = Subscribe(email=recipient)
            db.session.add(new_recipient)
            db.session.commit()

            msg = Message('PamantasanPH Newsletter', sender='@gmail.com', recipients=[recipient])
            msg.body = "Thank you for subscribing to our newsletter!"
            mail.send(msg)
            flash('Subscribed successfully!', category='success')
            return redirect(url_for('index'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash('You have already subscribed!', category='success')
            return redirect(url_for('index'))