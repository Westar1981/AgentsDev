"""
Application factory for the Multi-AI Agent Application.
"""
from flask import Flask
from flask_jwt_extended import JWTManager
from src.config.config import config
from src.config.database import DatabaseConfig
from src.database import db

# Initialize extensions
jwt = JWTManager()

def create_app(config_name='default'):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Set database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = DatabaseConfig.get_database_uri(config_name)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    # Register blueprints
    from src.auth import auth_bp
    from src.agents import agents_bp
    from src.tasks import tasks_bp
    from src.teams import teams_bp
    from src.monitoring import monitoring_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(agents_bp, url_prefix='/agents')
    app.register_blueprint(tasks_bp, url_prefix='/tasks')
    app.register_blueprint(teams_bp, url_prefix='/teams')
    app.register_blueprint(monitoring_bp, url_prefix='/monitoring')
    
    return app

def init_app():
    """Initialize the application."""
    app = create_app()
    return app

if __name__ == '__main__':
    app = init_app()
    app.run(debug=True)
