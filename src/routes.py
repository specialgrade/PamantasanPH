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
    @app.route('/home/universities')
    def universities():
        return render_template('univs.html')
    
    @app.route('/home/bookmarks')
    def bookmarks():
        return render_template('bookmarks.html')
    
    # route for sending email to the users
    @app.route('/newsletter', methods=['POST'])
    def newsletter():
        try:
            recipient = request.form.get('email')
            new_recipient = Subscribe(email=recipient)
            db.session.add(new_recipient)
            db.session.commit()

            msg = Message('DEAR SUBSCRIBERS,', sender='pamantasanph@gmail.com', recipients=[recipient])
            msg.body = '''Are you looking for universities that prioritize your growth and success? Look no further than Pamantasan PH! 
            
    Thank you for choosing Pamantasan PH as your trusted partner in discovering educational institutions that offer programs tailored to your interests and career goals. We're excited to continue this journey with you and can't wait to reveal the exciting updates that lie ahead!
            
    Here at Pamantasan PH, we understand the importance of providing a good and productive experience for our users. That's why we've been hard at work behind the scenes to ensure that every update and enhancement we introduce is designed with your needs in mind.
            
    Now, worry less because we got you!
            
    Warm Regards,
    PAMANTASAN PH TEAM'''
            mail.send(msg)
            flash("Subscribed successfully!")
            return redirect(url_for('index'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash("You have already subscribed!")
            return redirect(url_for('index'))
        
    # routes for separate univs
    @app.route('/home/universities/city-of-malabon-university', methods=['GET', 'POST'])
    def CMU():
        return render_template('CMU.html')
    
    @app.route('/home/universities/dr-filemon-c-aguilar-memorial-college-of-las-pinas', methods=['GET', 'POST'])
    def Dr_Fil():
        return render_template('dr.fil.html')
    
    @app.route('/home/universities/eulogio-amang-rodriguez-institute-of-science-&-technology', methods=['GET', 'POST'])
    def Earist():
        return render_template('earist.html')    
    
    @app.route('/home/universities/marikina-polytechnic-college', methods=['GET', 'POST'])
    def MPC():
        return render_template('mpc.html')
    
    @app.route('/home/universities/navotas-polytechnic-college', methods=['GET', 'POST'])
    def NPC():
        return render_template('npc.html')
    
    @app.route('/home/universities/paranaque-city-college', methods=['GET', 'POST'])
    def PCC():
        return render_template('pcc.html')
    
    @app.route('/home/universities/polytechnic-college-of-the-city-of Meycauayan', methods=['GET', 'POST'])
    def PCCM():
        return render_template('pccm.html')
    
    @app.route('/home/universities/pamantasan-ng-lungsod-ng-maynila', methods=['GET', 'POST'])
    def PLM():
        return render_template('plm.html')
    
    @app.route('/home/universities/pamantasan-ng-lungsod-ng-marikina', methods=['GET', 'POST'])
    def PLMAR():
        return render_template('plmar.html')
    
    @app.route('/home/universities/pamantasan-ng-lungsod-ng-muntinlupa', methods=['GET', 'POST'])
    def PLMUN():
        return render_template('plmun.html')
    
    @app.route('/home/universities/pamantasan-ng-lungsod-ng-pasig', methods=['GET', 'POST'])
    def PLP():
        return render_template('plp.html')
    
    @app.route('/home/universities/pamantasan-ng-lungsod-ng-valenzuela', methods=['GET', 'POST'])
    def PLV():
        return render_template('plv.html')
    
    @app.route('/home/universities/philippine-national-university', methods=['GET', 'POST'])
    def PNU():
        return render_template('pnu.html')
    
    @app.route('/home/universities/philippine-state-college-of-aeronautics', methods=['GET', 'POST'])
    def PSCA():
        return render_template('psca.html')
    
    @app.route('/home/universities/polytechnic-university-of-the-philippines', methods=['GET', 'POST'])
    def PUP():
        return render_template('pup.html')
    
    @app.route('/home/universities/quezon-city-university', methods=['GET', 'POST'])
    def QCU():
        return render_template('qcu.html')
    
    @app.route('/home/universities/taguig-city-university', methods=['GET', 'POST'])
    def TCU():
        return render_template('tcu.html')
    
    @app.route('/home/universities/technological-university-of-the-philippines', methods=['GET', 'POST'])
    def TUP():
        return render_template('tup.html')
    
    @app.route('/home/universities/universidad-de-manila', methods=['GET', 'POST'])
    def UDM():
        return render_template('udm.html')
    
    @app.route('/home/universities/university-of-makati', methods=['GET', 'POST'])
    def UM():
        return render_template('um.html')
    
    @app.route('/home/universities/university-of-the-philippines', methods=['GET', 'POST'])
    def UP():
        return render_template('up.html')