"""
Main application entry point for the Multi-AI Agent Application.
"""
from flask import Flask
from flask_jwt_extended import JWTManager
from src.config.config import config
from src.database import db, init_db, shutdown_session

# Initialize JWT
jwt = JWTManager()

def create_app(config_name='default'):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    
    # Initialize database
    init_db(app)
    
    # Register session cleanup
    app.teardown_appcontext(shutdown_session)
    
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
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
