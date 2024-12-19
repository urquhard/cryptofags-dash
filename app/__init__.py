from flask import Flask
from .config import Config
from .dashboard import init_dashboard

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    from .views import main_bp
    app.register_blueprint(main_bp)

    # Initialize the Dash app with the Flask server
    init_dashboard(app)

    return app
