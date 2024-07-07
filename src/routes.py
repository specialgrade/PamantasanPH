from flask import render_template, redirect, url_for, request, jsonify, render_template_string, flash, abort, session, current_app
from src.app import db, mail, bcrypt, oauth, login_manager
from src.forms import RegistrationForm, LoginForm, RequestResetForm, ResetPasswordForm, UpdateAccountForm, VerifyOTPForm
from src.models import Subscribe, User, University, Rating, Todo
from flask import send_from_directory
from flask_login import login_user, current_user, logout_user, login_required, UserMixin, LoginManager
from flask_mail import Message
from sqlalchemy.exc import SQLAlchemyError
import os
from PIL import Image
import random
import secrets
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv
import logging

load_dotenv()

email_sender = os.getenv('email')

def init_app(app):

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    logging.basicConfig(level=logging.DEBUG)

    google = oauth.google
    facebook = oauth.facebook
    
    # routes to go to the home page
    @app.route('/', methods=['GET', 'POST'])
    @app.route('/dashboard', methods=['GET', 'POST'])
    def dashboard():
        return render_template('dashboard.html', title='Dashboard', current_user=current_user)
    
    
    @app.route('/dashboard/map/', methods=['GET', 'POST'])
    def map():
        return render_template('map.html')
    
    @app.route('/dashboard/regions/', methods=['GET', 'POST'])
    def regions():
        return render_template('regions.html')
    
    # FOR PRIVACY
    @app.route('/register/privary-and-policy', methods=['GET', 'POST'])
    def privacy():
        return render_template('privacy.html')

    # teams 
    @app.route('/dashboard/teams/', methods=['GET', 'POST'])
    def teams():
        return render_template('teams.html')
    
    #settings
    @app.route('/dashboard/settings', methods=['GET', 'POST'])
    @login_required
    def settings():
        form = UpdateAccountForm()
        return render_template('settings.html', form=form)
    
    # REGISTER-LOGIN-LOGOUT--------------------------------------------------------------------------------
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        
        form = RegistrationForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            
            flash('Your account has been created! You are now able to log in.', 'success')
            return redirect(url_for('login'))  # Redirect to login page upon successful registration
        
        return render_template('register.html', title='Register', form=form)
    
    @app.route('/login', methods=['POST', 'GET'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('dashboard'))
            else:
                error_message = 'Login Unsuccessful. Please check email and password'
                return render_template('login.html', error_message=error_message, form=form)
        return render_template('login.html', form=form)
    
    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('login'))
    
    # FOR SAVING PROFILE PIC-------------------------------------------------------------------------
    def save_picture(form_picture):
        random_hex = secrets.token_hex(8)
        _, f_ext = os.path.splitext(form_picture.filename)
        picture_fn = random_hex + f_ext
        picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
        output_size = (125, 125)
        i = Image.open(form_picture)
        i.thumbnail(output_size)
        i.save(picture_path)
        return picture_fn

    # FOR UPDATING ACCOUNT INFORMATION----------------------------------------------------------------
    @app.route('/account', methods=['POST', 'GET'])
    @login_required
    def account():
        form = UpdateAccountForm()
        if form.validate_on_submit():
            if form.picture.data:
                picture_file = save_picture(form.picture.data)
                current_user.image_file = picture_file
            current_user.username = form.username.data
            current_user.email = form.email.data
            db.session.commit()
            flash("Your account has been updated", 'success')
            return redirect(url_for('dashboard'))
        elif request.method == 'GET':
            form.username.data = current_user.username
            form.email.data = current_user.email
        image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
        return render_template('dashboard.html', title='Account', form=form, image_file=image_file)
    
    def send_reset_email(user):
        token = user.get_reset_token()
        msg = Message('Password Reset Request', sender='MAIL_USERNAME', recipients=[user.email])
        email_body = render_template('reset_pw.txt', username=user.username)
        current_app.logger.info(f"Email body content: {email_body}")  # Log email body content
        msg.body = email_body
        mail.send(msg)


    @app.route('/reset_password', methods=['POST', 'GET'])
    def forgot_password():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        form = RequestResetForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            send_reset_email(user)
            flash('An email has been sent with a password reset link. Please check your inbox.', 'info')
            return redirect(url_for('login'))
        return render_template('forgotPassword.html', form=form, title='Reset Request')
    
    @app.route('/reset_password/<token>', methods=['POST', 'GET'])
    def reset_token(token):
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        user = User.verify_reset_token(token)
        if user is None:
            flash('This is an invalid or expired token. Please try again.', 'warning')
            return redirect(url_for('forgot_password'))
        form = ResetPasswordForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user.password = hashed_password
            db.session.commit()
            flash('Password has been reset. You can now log in with your new password.', 'info')
            return redirect(url_for('login'))
        return render_template('changePassword.html', form=form, title='Reset Password')

    
    
    
    # GOOGLE LOGIN-----------------------------------------------------------------------------------------
    
    @app.route('/login/google')
    def google_login():
        redirect_uri = url_for('google_authorize', _external=True)
        return google.authorize_redirect(redirect_uri)

    @app.route('/authorize/google')
    def google_authorize():
        token = google.authorize_access_token()
        resp = google.get('https://www.googleapis.com/oauth2/v1/userinfo')
        user_info = resp.json()
        user = User.query.filter_by(email=user_info['email']).first()
        if user is None:
            user = User(
                username=user_info['name'],
                email=user_info['email'],
                password=bcrypt.generate_password_hash('google_oauth_password').decode('utf-8')
            )
            db.session.add(user)
            db.session.commit()
        login_user(user)
        return redirect(url_for('dashboard'))
    
    # FACEBOOK LOGIN---------------------------------------------------------------------------------------

    @app.route('/login/facebook')
    def facebook_login():
        redirect_uri = url_for('facebook_authorize', _external=True)
        return facebook.authorize_redirect(redirect_uri)
    
    @app.route('/authorize/facebook')
    def facebook_authorize():
        token = facebook.authorize_access_token()
        resp = facebook.get('me?fields=id,name,email')
        user_info = resp.json()
        user = User.query.filter_by(email=user_info['email']).first()
        if user is None:
            user = User(
                username=user_info['name'],
                email=user_info['email'],
                password=bcrypt.generate_password_hash('facebook_oauth_password').decode('utf-8')
                )
            db.session.add(user)
            db.session.commit()
        login_user(user)
        return redirect(url_for('dashboard'))
    
   
    
    # FOR TO-DO FEATURE================================================================
    @app.route('/dashboard/todo')
    @login_required
    def todo():
        todo_list = Todo.query.filter_by(user_id=current_user.id).all()
        return render_template('dashboard.html', todo_list=todo_list)
    
    @app.route('/add_task', methods=['POST'])
    @login_required
    def add_task():
        task = request.form['task']
        new_task = Todo(task=task, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('todo'))
    
    @app.route('/update_task/<int:task_id>')
    @login_required
    def update_task(task_id):
        todo = Todo.query.get_or_404(task_id)
        if todo.user_id != current_user.id:
            return 'Unauthorized access'
        
        todo.status = not todo.status
        db.session.commit()
        return redirect(url_for('todo'))
    
    @app.route('/delete_task/<int:task_id>')
    @login_required
    def delete_task(task_id):
        todo = Todo.query.get_or_404(task_id)
        if todo.user_id != current_user.id:
            return 'Unauthorized access'
        
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for('todo'))





    # =========================================================================================
    
    
    # route for sending email to the users
    @app.route('/newsletter', methods=['POST'])
    def newsletter():
        try:
            recipient = request.form.get('email')
            new_recipient = Subscribe(email=recipient)
            db.session.add(new_recipient)
            db.session.commit()
            
            subscriber_name = current_user.username if current_user.is_authenticated else 'Subscriber'
            
            with app.open_resource('templates/subscription.txt') as file:
                email_template = file.read().decode('utf-8')
                rendered_email = render_template_string(email_template, subscriber_name=subscriber_name)
                
                msg = Message('PamantasanPH Newsletter', sender=email_sender, recipients=[recipient])
                msg.body = rendered_email
                mail.send(msg)
                return redirect(url_for('dashboard'))
        except SQLAlchemyError as e:
            db.session.rollback()
            return redirect(url_for('dashboard'))
        
    @app.route('/check_email', methods=['POST'])
    def check_email():
        email = request.json.get('email')
        # Check if the email exists in the database
        exists = db.session.query(Subscribe.query.filter_by(email=email).exists()).scalar()
        return jsonify({'exists': exists})
        
    # ROUTES FOR SEPARATE HTMLS===================================================================
    
    @app.route('/university/regions/<string:university_id>')
    @login_required
    def universityDeets(university_id):
        file_path = os.path.join(app.root_path, 'templates', f'{university_id}.html')
        
        if os.path.exists(file_path):
            return render_template(f'{university_id}.html')
        else:
            abort(404)
    
    @app.route('/university-public/regions/<string:university_id>')
    def universityDeetsPublic(university_id):
        file_path = os.path.join(app.root_path, 'templates', f'{university_id}.html')
        
        if os.path.exists(file_path):
            return render_template(f'{university_id}.html')
        else:
            abort(404)

    # FOR COMPARE FEATURE=========================================================================

    # Map Univ names to their respective html filename
    university_files = {
        'CITY-OF-MALABON-UNIVERSITY': 'cmu.html',
        'DR-FILEMON-C-AGUILAR-MEMORIAL-COLLEGE-OF-LAS-PIÑAS': 'dfcamclp.html',
        'EULOGIO-AMANG-RODRIGUEZ-INSTITUTE-OF-SCIENCE-AND-TECHNOLOGY': 'earist.html',
        'MARIKINA-POLYTECHNIC-COLLEGE': 'mpc.html',
        'NAVOTAS-POLYTECHNIC-COLLEGE': 'npc.html',
        'PAMANTASAN-NG-LUNGSOD-NG-MARIKINA': 'plmar.html',
        'PAMANTASAN-NG-LUNGSOD-NG-MAYNILA': 'plm.html',
        'PAMANTASAN-NG-LUNGSOD-NG-MUNTINLUPA': 'plmun.html',
        'PAMANTASAN-NG-LUNGSOD-NG-PASIG': 'plp.html',
        'PAMANTASAN-NG-VALENZUELA': 'pv.html',
        'PARAÑAQUE-CITY-COLLEGE': 'pcc.html',
        'PHILIPPINE-NORMAL-UNIVERSITY': 'pnu.html',
        'PHILIPPINE-STATE-COLLEGE-OF-AERONAUTICS': 'philsca.html',
        'POLYTECHNIC-COLLEGE-OF-THE-CITY-OF-MEYCAUAYAN': 'pccm.html',
        'POLYTECHNIC-UNIVERSITY-OF-THE-PHILIPPINES': 'pup.html',
        'QUEZON-CITY-UNIVERSITY': 'qcu.html',
        'TAGUIG-CITY-UNIVERSITY': 'tcu.html',
        'TECHNOLOGICAL-UNIVERSITY-OF-THE-PHILIPPINES': 'tup.html',
        'UNIVERSIDAD-DE-MANILA': 'udm.html',
        'UNIVERSITY-OF-MAKATI': 'umak.html',
        'UNIVERSITY-OF-THE-PHILIPPINES': 'up.html',
        'ADIONG-MEMORIAL-STATE-COLLEGE': 'amsc.html',
        'BALABAGAN-TRADE-SCHOOL': 'bts.html',
        'BASILAN-STATE-COLLEGE': 'bsc.html',
        'COTABATO-FOUNDATION-COLLEGE-OF-SCIENCE-AND-TECHNOLOGY': 'cfcst.html',
        'COTABATO-STATE-UNIVERSITY': 'csu.html',
        'HADJI-BUTU-SCHOOL-OF-ARTS-AND-TRADES': 'hbsat.html',
        'LANAO-AGRICULTURAL-COLLEGE': 'lac.html',
        'LAPAK-AGRICULTURAL-SCHOOL': 'las.html',
        'MINDANAO-STATE-UNIVERSITY': 'msu.html',
        'REGIONAL-MADRASAH-GRADUATE-ACADEMY': 'rmga.html',
        'SULU-STATE-COLLEGE': 'ssc.html',
        'TAWI-TAWI-REGIONAL-AGRICULTURAL-COLLEGE': 'trac.html',
        'UNDA-MEMORIAL-NATIONAL-AGRICULTURAL-SCHOOL': 'umnas.html',
        'UNIVERSITY-OF-SOUTHERN-MINDANAO': 'usm.html',
        'UPI-AGRICULTURAL-SCHOOL': 'uas.html',
        'ABRA-STATE-INSTITUTE-OF-SCIENCE-AND-TECHNOLOGY': 'asist.html',
        'APAYAO-STATE-COLLEGE': 'asc.html',
        'BENGUET-STATE-UNIVERSITY': 'bsu.html',
        'IFUGAO-STATE-UNIVERSITY': 'ifsu.html',
        'KALINGA-STATE-UNIVERSITY': 'ksu.html',
        'MOUNTAIN-PROVINCE-STATE-UNIVERSITY': 'mpsu.html',
        'PHILIPPINE-MILITARY-ACADEMY': 'pma.html',
        'BINALATONGAN-COMMUNITY-COLLEGE': 'bcc.html',
        'DON-MARIANO-MARCOS-MEMORIAL-STATE-UNIVERSITY': 'dmmmsu.html',
        'ILOCOS-SUR-POLYTECHNIC-STATE-COLLEGE': 'ispsc.html',
        'MARIANO-MARCOS-STATE-UNIVERSITY': 'mmsu.html',
        'PANGASINAN-STATE-UNIVERSITY': 'psu.html',
        'UNIVERSITY-OF-NORTHERN-PHILIPPINES': 'unp.html',
        'BATANES-STATE-COLLEGE': 'bsc.html',
        'CAGAYAN-STATE-UNIVERSITY': 'csu.html',
        'ISABELA-STATE-UNIVERSITY': 'isu.html',
        'NUEVA-VIZCAYA-STATE-UNIVERSITY': 'nvsu.html',
        'QUIRINO-STATE-UNIVERSITY': 'qsu.html',
        'BULACAN-AGRICULTURAL-STATE-COLLEGE': 'basc.html',
        'BULACAN-STATE-UNIVERSITY': 'bsu.html',
        'CENTRAL-LUZON-STATE-UNIVERSITY': 'clsu.html',
        'DON-HONORIO-VENTURA-STATE-UNIVERSITY': 'dhvsu.html',
        'NUEVA-ECIJA-UNIVERSITY-OF-SCIENCE-AND-TECHNOLOGY': 'neust.html',
        'BATANGAS-STATE-UNIVERSITY': 'batsu.html',
        'CAVITE-STATE-UNIVERSITY': 'cvsu.html',
        'LAGUNA-STATE-POLYTECHNIC-UNIVERSITY': 'lspu.html',
        'SOUTHERN-LUZON-STATE-UNIVERSITY': 'slsu.html',
        'UNIVERSITY-OF-RIZAL-SYSTEM': 'urs.html',
        'BACO-COMMUNITY-COLLEGE': 'bcc.html',
        'CITY-COLLEGE-OF-CALAPAN': 'ccc.html',
        'MARINDUQUE-STATE-COLLEGE': 'msc.html',
        'MINDORO-STATE-UNIVERSITY': 'minsu.html',
        'OCCIDENTAL-MINDORO-STATE-COLLEGE': 'omsc.html',\
        'PALAWAN-STATE-UNIVERSITY': 'psu.html',
        'POLA-COMMUNITY-COLLEGE': 'pcc.html',
        'ROMBLON-STATE-UNIVERSITY': 'rsu.html',
        'WESTERN-PHILIPPINES-UNIVERSITY': 'wpu.html',
        'BICOL-STATE-COLLEGE-OF-APPLIED-SCIENCES-AND-TECHNOLOGY': 'biscast.html',
        'BICOL-UNIVERSITY': 'bu.html',
        'CATANDUANES-STATE-UNIVERSITY': 'csu.html',
        'CENTRAL-BICOL-STATE-UNIVERSITY-OF-AGRICULTURE': 'cbsua.html',
        'PARTIDO-STATE-UNIVERSITY': 'parsu.html',
        'BAGO-CITY-COLLEGE': 'bcc.html',
        'CARLOS-HILADO-MEMORIAL-STATE-UNIVERSITY': 'chmsu.html',
        'LA-CARLOTA-CITY-COLLEGE': 'lccc.html',
        'PHILIPPINE-NORMAL-UNIVERSITY': 'pnu.html',
        'WEST-VISAYAS-STATE-UNIVERSITY': 'wvsu.html',
        'BOHOL-ISLAND-STATE-UNIVERSITY': 'bisu.html',
        'CEBU-NORMAL-UNIVERSITY': 'cnu.html',
        'CEBU-TECHNOLOGICAL-UNIVERSITY': 'ctu.html',
        'NEGROS-ORIENTAL-STATE-UNIVERSITY': 'norsu.html',
        'SIQUIJOR-STATE-COLLEGE': 'ssc.html',
        'EASTERN-SAMAR-STATE-UNIVERSITY': 'essu.html',
        'EASTERN-VISAYAS-STATE-UNIVERSITY': 'evsu.html',
        'LEYTE-NORMAL-UNIVERSITY': 'lnu.html',
        'PALOMPON-INSTITUTE-OF-TECHNOLOGY': 'pit.html',
        'UNIVERSITY-OF-EASTERN-PHILIPPINES': 'uep.html',
        'BASILAN-STATE-COLLEGE': 'bsc.html',
        'JH-CERILLES-STATE-COLLEGE': 'jhcs.html',
        'JOSE-RIZAL-MEMORIAL-STATE-UNIVERSITY': 'jrmsu.html',
        'WESTERN-MINDANAO-STATE-UNIVERSITY': 'wmsu.html',
        'ZAMBOANGA-STATE-COLLEGE-OF-MARINE-SCIENCES-AND-TECHNOLOGY': 'zscmst.html',
        'BUKIDNON-STATE-UNIVERSITY': '_bukidnon.html',
        'CENTRAL-MINDANAO-UNIVERSITY': 'cmu.html',
        'CAMIGUIN-POLYTECHNIC-STATE-COLLEGE': 'cpoly.html',
        'NORTHWESTERN-MINDANAO-STATE-COLLEGE-OF-SCIENCE-AND-TECHNOLOGY': 'nmscst.html',
        'UNIVERSITY-OF-SCIENCE-AND-TECHNOLOGY-OF-SOUTHERN-PHILIPPINES': 'ustsp.html',
        'DAVAO-DEL-NORTE-STATE-COLLEGE': 'ddnsc.html',
        'DAVAO-DEL-SUR-STATE-COLLEGE': 'ddssc.html',
        'DAVAO-ORIENTAL-STATE-UNIVERSITY': 'dosu.html',
        'SOUTHERN-PHILIPPINES-AGRI-BUSINESS-MARINE-AND-AQUATIC-SCHOOL-OF-TECHNOLOGY': 'spamast.html',
        'UNIVERSITY-OF-SOUTHEASTERN-PHILIPPINES': 'usep.html',
        'COTABATO-FOUNDATION-COLLEGE-OF-SCIENCE-AND-TECHNOLOGY': 'cfcst.html',
        'SOUTH-COTABATO-STATE-COLLEGE': 'scsc.html',
        'SULTAN-KUDARAT-STATE-UNIVERSITY': 'sksu.html',
        'UNIVERSITY-OF-SOUTHERN-MINDANAO': 'usm.html',
        'AGUSAN-DEL-SUR-STATE-COLLEGE-OF-AGRICULTURE-AND-TECHNOLOGY': 'ascat.html',
        'CARAGA-STATE-UNIVERSITY': 'csu.html',
        'HINATUAN-SOUTHERN-COLLEGE': 'hsc.html',
        'NORTH-EASTERN-MINDANAO-STATE-UNIVERSITY': 'nemsu.html',
        'SURIGAO-DEL-NORTE-STATE-UNIVERSITY': 'suns.html'
    }
    
    @app.route('/dashboard/compare', methods=['GET', 'POST'])
    @login_required
    def compare():
        return render_template('compare.html')
    
    @app.route('/university/<name>')
    @login_required
    def get_university_html(name):
        file_name = university_files.get(name)
        if file_name:
            return send_from_directory('templates', file_name)
        else:
            abort(404)

    # ROUTES FOR REGIONS========================================================

    @app.route('/dashboard/regions/region-1', methods=['POST', 'GET'])
    @login_required
    def region1():
        return render_template('region1.html')
    
    @app.route('/dashboard/regions/region-2', methods=['POST', 'GET'])
    @login_required
    def region2():
        return render_template('region2.html')
    
    @app.route('/dashboard/regions/region-3', methods=['POST', 'GET'])
    @login_required
    def region3():
        return render_template('region3.html')
    
    @app.route('/dashboard/regions/region-4a', methods=['POST', 'GET'])
    @login_required
    def region4a():
        return render_template('region4a.html')
    
    @app.route('/dashboard/regions/region-4b', methods=['POST', 'GET'])
    @login_required
    def region4b():
        return render_template('region4b.html')
    
    @app.route('/dashboard/regions/region-5', methods=['POST', 'GET'])
    @login_required
    def region5():
        return render_template('region5.html')
    
    @app.route('/dashboard/regions/region-6', methods=['POST', 'GET'])
    @login_required
    def region6():
        return render_template('region6.html')
    
    @app.route('/dashboard/regions/region-7', methods=['POST', 'GET'])
    @login_required
    def region7():
        return render_template('region7.html')
    
    @app.route('/dashboard/regions/region-8', methods=['POST', 'GET'])
    @login_required
    def region8():
        return render_template('region8.html')
    
    @app.route('/dashboard/regions/region-9', methods=['POST', 'GET'])
    @login_required
    def region9():
        return render_template('region9.html')
    
    @app.route('/dashboard/regions/region-10', methods=['POST', 'GET'])
    @login_required
    def region10():
        return render_template('region10.html')
    
    @app.route('/dashboard/regions/region-11', methods=['POST', 'GET'])
    @login_required
    def region11():
        return render_template('region11.html')
    
    @app.route('/dashboard/regions/region-12', methods=['POST', 'GET'])
    @login_required
    def region12():
        return render_template('region12.html')
    
    @app.route('/dashboard/regions/region-13', methods=['POST', 'GET'])
    @login_required
    def region13():
        return render_template('region13.html')
    
    @app.route('/dashboard/regions/region-ncr', methods=['POST', 'GET'])
    def ncr():
        return render_template('ncr.html')
    
    @app.route('/dashboard/regions/region-car', methods=['POST', 'GET'])
    @login_required
    def cordillera():
        return render_template('cordillera.html')
    
    @app.route('/dashboard/regions/region-barmm', methods=['POST', 'GET'])
    @login_required
    def bangsamoro():
        return render_template('bangsamoro.html')
    
