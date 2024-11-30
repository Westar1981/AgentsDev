"""
Routes for system monitoring in the Multi-AI Agent Application.
"""
from flask import jsonify
from src.monitoring import monitoring_bp

@monitoring_bp.route('/', methods=['GET'])
def get_system_status():
    """Temporary route for testing."""
    return jsonify({
        "message": "Monitoring module initialized",
        "status": "operational"
    }), 200

@monitoring_bp.route('/health', methods=['GET'])
def health_check():
    """Basic health check endpoint."""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }), 200
