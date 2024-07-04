from flask import render_template, redirect, url_for, request, jsonify, render_template_string, flash
from src.app import db, mail, bcrypt, oauth
from src.forms import RegistrationForm, LoginForm, RequestResetForm, ResetPasswordForm, UpdateAccountForm, RatingForm
from src.models import Subscribe, User, University, Rating, Todo
from flask import send_from_directory
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
from sqlalchemy.exc import SQLAlchemyError
import os
from PIL import Image
import random
import secrets
from dotenv import load_dotenv

load_dotenv()

email_sender = os.getenv('email')

def init_app(app):

    google = oauth.google
    facebook = oauth.facebook
    
    # routes to go to the home page
    @app.route('/', methods=['GET', 'POST'])
    @app.route('/dashboard', methods=['GET', 'POST'])
    def dashboard():
        return render_template('dashboard.html')
    
    # compare feature
    @app.route('/dashboard/compare/', methods=['GET', 'POST'])
    def compare():
        return render_template('compare.html')


    # teams 
    @app.route('/dashboard/teams/', methods=['GET', 'POST'])
    def teams():
        return render_template('teams.html')
    
    # REGISTER-LOGIN-LOGOUT--------------------------------------------------------------------------------
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegistrationForm()
        print(form)
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data, password=hashed_password, email=form.email.data)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You are now able to login', 'success')
            return redirect(url_for('login'))
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
                flash('Login Unsuccessful. Please check email and password', 'danger')
        return render_template('login.html', title='Login', form=form)
    
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
    
    otp_storage = {}
    
    def send_otp_email(user):
        global otp
        otp = random.randint(1000, 9999)
        otp_storage[user.email] = otp
        msg = Message('Password Change Request', sender=os.getenv('MAIL_USERNAME'), recipients=[user.email])
        with open('reset_pw.txt', 'r') as file:
            email_message = file.read().strip()
        email_message = email_message.replace('{user.username}', user.username)
        email_message = email_message.replace('{otp}', str(otp))
        msg.body = email_message
        mail.send(msg)
        
    @app.route('/reset_password', methods=['GET', 'POST'])
    def reset_request():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        
        if request.method == 'POST':
            email = request.form.get('email')
            user = User.query.filter_by(email=email).first()
            if user:
                send_otp_email(user)
                return render_template('forgotPassword.html', email=email)
            else:
                flash('Invalid email address. Please check your information and try again.', 'warning')
        
        return render_template('forgotPassword.html')

    @app.route('/verify_otp', methods=['GET', 'POST'])
    def verify_otp():
        email = request.form.get('email')
        entered_otp = request.form.get('otp')
        if email in otp_storage and otp_storage[email] == int(entered_otp):
            flash('OTP verified. You can now reset your password.', 'success')
            return redirect(url_for('reset_request', email=email))
        else:
            flash('Invalid OTP. Please try again.', 'danger')
            return render_template('verifyEmail.html', email=email)
        
    @app.route('/resend_otp', methods=['POST'])
    def resend_otp():
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            send_otp_email(user)
            flash('A new OTP has been sent to your email.', 'info')
            return render_template('verifyEmail.html', email=email)
    
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
    
    # FOR STAR RATINGS---------------------------------------------------------------------

    @app.route('/university/<int:university_id>', methods=['GET', 'POST'])
    def university(university_id):
        university = University.query.get_or_404(university_id)
        rating_form = RatingForm()
        
        if rating_form.validate_on_submit():
            user_id = current_user.id
            rating_value = rating_form.rating.data
            
            existing_rating = Rating.query.filter_by(user_id=user_id, university_id=university_id).first()
            if existing_rating:
                flash('You have already rated this university.', 'error')
            else:
                # Create a new rating entry
                new_rating = Rating(user_id=user_id, university_id=university_id, rating=rating_value)
                db.session.add(new_rating)
                db.session.commit()
                flash('Your rating has been submitted.', 'success')
                
                return redirect(url_for('university', university_id=university_id))
            
        ratings = Rating.query.filter_by(university_id=university_id).all()
        
        if ratings:
            total_ratings = len(ratings)
            sum_ratings = sum([rating.rating for rating in ratings])
            average_rating = sum_ratings / total_ratings
        else:
            average_rating = 0 

        template_name = f'universities/{university.name.lower()}.html'
        
        return render_template(template_name, university=university, average_rating=average_rating, rating_form=rating_form)
    
    # FOR TO-DO FEATURE================================================================
    @app.route('dashboard/todo')
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

            with open('subscription.txt', 'r') as file:
                email_template = file.read()

            subscriber_name = current_user.username
            rendered_email = render_template_string(email_template, subscriber_name=subscriber_name)

            msg = Message('PamantasanPH Newsletter', sender=os.getenv('MAIL_USERNAME'), recipients=[recipient])
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