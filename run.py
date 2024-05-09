from flask import Flask, render_template
from src.app import create_app
from src import routes
from flask_mail import Mail

app = create_app()

mail = Mail(app)

routes.init_app(app)

if __name__ == '__main__':
    app.run(debug = True)