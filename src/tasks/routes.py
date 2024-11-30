"""
Routes for task management in the Multi-AI Agent Application.
"""
from flask import jsonify
from src.tasks import tasks_bp

@tasks_bp.route('/', methods=['GET'])
def list_tasks():
    """Temporary route for testing."""
    return jsonify({"message": "Task management module initialized"}), 200
