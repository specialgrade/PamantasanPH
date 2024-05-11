from flask import Flask, render_template, redirect, url_for, request
from .app import db, mail, create_app
from .models import Subscribe
from flask import send_from_directory
from flask_mail import Message, Mail
from sqlalchemy.exc import SQLAlchemyError
#from dotenv import load_dotenv
#import os
#load_dotenv('.env')

#email_sender = os.getenv('EMAIL')

def init_app(app):
    
    # routes to go to the home page
    @app.route('/home', methods=['GET', 'POST'])
    @app.route('/', methods=['GET', 'POST'])
    def index():
        return render_template('index.html')
    
    @app.route('/home', methods=['GET', 'POST'])
    def home():
        return render_template('index.html')
    
    # routes to render the univs.html when they click the Universities button from the home page
    @app.route('/home/universities', methods=['GET'])
    def universities():
        return render_template('univs.html')
    


    # routes for specific universities
    @app.route('/home/universities/city-of-malabon-university', methods=['GET', 'POST'])
    def CMU():
        return render_template('/univs/CMU.html')
    
    @app.route('/home/universities/dr-filemon-c-aguilar-memorial-college-of-las-pinas', methods=['GET', 'POST'])
    def Dr_Fil():
        return render_template('/univs/dr.fil.html')
    
    @app.route('/home/universities/eulogio-"amang"-rodriguez-institute-of-science-&-technology', methods=['GET', 'POST'])
    def Earist():
        return render_template('/univs/earist.html')    
    
    @app.route('/home/universities/marikina-polytechnic-college', methods=['GET', 'POST'])
    def MPC():
        return render_template('/univs/mpc.html')
    
    @app.route('/home/universities/navotas-polytechnic-college', methods=['GET', 'POST'])
    def NPC():
        return render_template('/univs/npc.html')
    
    @app.route('/home/universities/paranaque-city-college', methods=['GET', 'POST'])
    def PCC():
        return render_template('/univs/pcc.html')
    
    @app.route('/home/universities/polytechnic-college-of-the-city-of Meycauayan', methods=['GET', 'POST'])
    def PCCM():
        return render_template('/univs/pccm.html')
    
    @app.route('/home/universities/pamantasan-ng-lungsod-ng-maynila', methods=['GET', 'POST'])
    def PLM():
        return render_template('/univs/plm.html')
    
    @app.route('/home/universities/pamantasan-ng-lungsod-ng-marikina', methods=['GET', 'POST'])
    def PLMAR():
        return render_template('/univs/plmar.html')
    
    @app.route('/home/universities/pamantasan-ng-lungsod-ng-muntinlupa', methods=['GET', 'POST'])
    def PLMUN():
        return render_template('/univs/plmun.html')
    
    @app.route('/home/universities/pamantasan-ng-lungsod-ng-pasig', methods=['GET', 'POST'])
    def PLP():
        return render_template('/univs/plp.html')
    
    @app.route('/home/universities/pamantasan-ng-lungsod-ng-valenzuela', methods=['GET', 'POST'])
    def PLV():
        return render_template('/univs/plv.html')
    
    @app.route('/home/universities/philippine-national-university', methods=['GET', 'POST'])
    def PNU():
        return render_template('/univs/pnu.html')
    
    @app.route('/home/universities/philippine-state-college-of-aeronautics', methods=['GET', 'POST'])
    def PSCA():
        return render_template('/univs/psca.html')
    
    @app.route('/home/universities/polytechnic-university-of-the-philippines', methods=['GET', 'POST'])
    def PUP():
        return render_template('/univs/pup.html')
    
    @app.route('/home/universities/quezon-city-university', methods=['GET', 'POST'])
    def QCU():
        return render_template('/univs/qcu.html')
    
    @app.route('/home/universities/taguig-city-university', methods=['GET', 'POST'])
    def TCU():
        return render_template('/univs/tcu.html')
    
    @app.route('/home/universities/technological-university-of-the-philippines', methods=['GET', 'POST'])
    def TUP():
        return render_template('/univs/tup.html')
    
    @app.route('/home/universities/universidad-de-manila', methods=['GET', 'POST'])
    def UDM():
        return render_template('/univs/udm.html')
    
    @app.route('/home/universities/university-of-makati', methods=['GET', 'POST'])
    def UM():
        return render_template('/univs/um.html')
    
    @app.route('/home/universities/university-of-the-philippines', methods=['GET', 'POST'])
    def UP():
        return render_template('/univs/up.html')
    


    # routes to render the favs.html when the user click the favorites button/nav
    @app.route('/home/bookmarks', methods=['GET', 'POST'])
    def bookmarks():
        return render_template('bookmarks.html')


    @app.route('/newsletter', methods=['POST'])
    def newsletter():
        try:
            recipient = request.form.get('email')
            new_recipient = Subscribe(email=recipient)
            db.session.add(new_recipient)
            db.session.commit()

            msg = Message('Hello world', sender="gmail.com", recipients=[recipient])
            msg.body = "This is a message from Flask"
            mail.send(msg)
            return "<h1>NADALI RIN</h1>"
        except SQLAlchemyError as e:
            db.session.rollback()  # Rollback the session in case of an error
            return f"Error: {str(e)}"

# THIS IS THE WORKING NEWSLETTER ROUTE ----------------------------------------------------------------
    #@app.route('/newsletter', methods=['POST'])
    #def newsletter():
        #recipient = request.form.get('email')             
        #new_recipient = Subscribe(email=recipient)
        #db.session.add(new_recipient)
        #db.session.commit()

        #msg = Message('Hello world', sender="pamantasanph@gmail.com", recipients=[recipient])
        #msg.body = "This is a message from Flask"
        #mail.send(msg)
        #return "<h1>NADALI RIN</h1>"
