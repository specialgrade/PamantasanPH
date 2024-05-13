from src.app import create_app
from src import routes

app = create_app()

routes.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True, use_reloader=True)