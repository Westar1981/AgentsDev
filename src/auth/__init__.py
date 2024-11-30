"""
Authentication module for the Multi-AI Agent Application.
"""
from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

from . import routes  # noqa
