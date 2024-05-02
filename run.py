from flask import Flask, render_template
from static.app import create_app
from static import routes

app = create_app()

routes.init_app(app)

if __name__ == '__main__':
    app.run(debug = True)