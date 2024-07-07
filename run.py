from src.app import create_app 
from src import routes
from flask_login import login_manager

app = create_app()

routes.init_app(app)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')