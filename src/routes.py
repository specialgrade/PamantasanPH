from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template("index.html")