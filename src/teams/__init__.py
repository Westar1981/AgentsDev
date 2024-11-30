"""
Team management module initialization.
"""
from flask import Blueprint

teams_bp = Blueprint('teams', __name__)

# Import routes after Blueprint creation to avoid circular imports
from src.teams import routes
