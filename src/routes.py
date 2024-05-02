from flask import Flask, render_template, redirect, url_for, request
from .app import db
from .models import Subscribe
from flask import send_from_directory

def init_app(app):

    @app.route('/')
    def index():
        return render_template('index.html')
    