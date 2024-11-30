"""
Agent management module initialization.
"""
from flask import Blueprint

agents_bp = Blueprint('agents', __name__)

from src.agents import routes  # Import routes after Blueprint creation
