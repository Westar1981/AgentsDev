"""
Test configuration and fixtures for the Multi-AI Agent Application.
"""
import pytest
from src.app import create_app, db
from src.auth.models import User
from werkzeug.security import generate_password_hash

@pytest.fixture
def app():
    """Create and configure a test application instance."""
    app = create_app('testing')
    
    # Create application context
    with app.app_context():
        # Create database tables
        db.create_all()
        
        # Create test user
        test_user = User(
            email='test@example.com',
            password=generate_password_hash('password123'),
            role='user'
        )
        db.session.add(test_user)
        db.session.commit()
        
        yield app
        
        # Clean up
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Create a test client."""
    return app.test_client()

@pytest.fixture
def auth_token(client):
    """Get authentication token for test user."""
    response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    return response.json['access_token']

@pytest.fixture
def auth_headers(auth_token):
    """Get headers with authentication token."""
    return {'Authorization': f'Bearer {auth_token}'}
