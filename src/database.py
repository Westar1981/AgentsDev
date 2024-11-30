"""
Database configuration and initialization for the Multi-AI Agent Application.
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker

# Initialize SQLAlchemy instance
db = SQLAlchemy()

# Create scoped session
Session = scoped_session(sessionmaker())

def init_db(app):
    """Initialize the database with the Flask app."""
    db.init_app(app)
    Session.configure(bind=db.engine)
    
    # Import models here to ensure they are registered with SQLAlchemy
    from src.auth.models import User
    
    # Create tables
    with app.app_context():
        db.create_all()

def shutdown_session(exception=None):
    """Remove the session at the end of each request."""
    Session.remove()
