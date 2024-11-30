"""
Task management module initialization.
"""
from flask import Blueprint

tasks_bp = Blueprint('tasks', __name__)

# Import routes after Blueprint creation to avoid circular imports
from src.tasks import routes
