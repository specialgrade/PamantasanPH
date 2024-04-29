from flask import Flask

# initializing all the files under src to a python package
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'PamantasanPH'

    return app