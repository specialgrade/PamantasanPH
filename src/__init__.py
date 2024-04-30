from flask import Flask

# initializing all the files under src to a python package
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'PamantasanPH'

    from .routes import routes

    app.register_blueprint(routes, url_prefix = '/')

    return app