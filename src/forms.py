from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from .models import User
from wtforms.widgets import html_params
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose another one.')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose another one.')
        
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    def validate_password(self, password):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(password.data):
            raise ValidationError('Incorrect password.')
        
class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. Please register first.')
        
class ResetPasswordForm(FlaskForm):
     confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
     password = PasswordField('Password', validators=[DataRequired()])
     submit = SubmitField('Reset Password')
            

class VerifyOTPForm(FlaskForm):
    otp = StringField('OTP', validators=[DataRequired()])
    digit1 = StringField('Digit 1', validators=[
        DataRequired(), Length(min=1, max=1),
        Regexp('^[0-9]$', message="Please enter a digit (0-9) only.")
    ])
    digit2 = StringField('Digit 2', validators=[
        DataRequired(), Length(min=1, max=1),
        Regexp('^[0-9]$', message="Please enter a digit (0-9) only.")
    ])
    digit3 = StringField('Digit 3', validators=[
        DataRequired(), Length(min=1, max=1),
        Regexp('^[0-9]$', message="Please enter a digit (0-9) only.")
    ])
    digit4 = StringField('Digit 4', validators=[
        DataRequired(), Length(min=1, max=1),
        Regexp('^[0-9]$', message="Please enter a digit (0-9) only.")
    ])
    submit = SubmitField('Verify')
