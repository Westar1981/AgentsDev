"""
System monitoring module initialization.
"""
from flask import Blueprint

monitoring_bp = Blueprint('monitoring', __name__)

# Import routes after Blueprint creation to avoid circular imports
from src.monitoring import routes
