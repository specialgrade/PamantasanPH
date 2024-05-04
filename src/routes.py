from flask import Flask, render_template, redirect, url_for, request, flash
from .app import db
from .models import Subscribe
from flask import send_from_directory
from flask_mail import Mail, Message

def init_app(app):
    
    # routes to go to the home page
    @app.route('/home', methods=['GET', 'POST'])
    @app.route('/', methods=['GET', 'POST'])
    def index():
        return render_template('index.html')
    
    # routes to render the univs.html when they click the Universities button from the home page
    @app.route('/universities', methods=['GET', 'POST'])
    def universities():
        return render_template('univs.html')
    
    # routes to redirect back to the homepage when the users click the email submit button 
    @app.route('/newsletter', methods = ['POST', 'GET'])
    def newsletter(): 
        if request.referrer.endswith('/home'):
            return redirect(url_for('index'))
        elif request.referrer.endswith('/universities'):
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))

        #if request.method == 'POST':
        #    msg = Message("PamantasanPH Tester", sender='pamantasanph@gmail.com', recipients=['ellasimara02@gmail.com'])
        #    msg.body = "Newsletter subscription email tester."
        #    msg.send(msg)
        #    return "<h1>Lol it works</h1>"
        #return redirect(url_for('index'))