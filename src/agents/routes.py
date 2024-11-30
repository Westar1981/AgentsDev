"""
Routes for agent management in the Multi-AI Agent Application.
"""
from flask import jsonify
from src.agents import agents_bp

@agents_bp.route('/', methods=['GET'])
def list_agents():
    """Temporary route for testing."""
    return jsonify({"message": "Agent management module initialized"}), 200
