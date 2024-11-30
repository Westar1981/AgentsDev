"""
Models for AI Agent management in the Multi-AI Agent Application.
"""
from datetime import datetime
from src.database import db

class Agent(db.Model):
    """Model for AI Agents in the system."""
    __tablename__ = 'agents'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), nullable=False, default='inactive')  # inactive, active, busy, error
    skills = db.Column(db.JSON, nullable=False, default=list)
    performance_metrics = db.Column(db.JSON, nullable=False, default=dict)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    creator = db.relationship('User', backref=db.backref('agents', lazy=True))
    
    def __repr__(self):
        """String representation of the Agent model."""
        return f'<Agent {self.name}>'
    
    def to_dict(self):
        """Convert agent object to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'status': self.status,
            'skills': self.skills,
            'performance_metrics': self.performance_metrics,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    @staticmethod
    def get_by_id(agent_id):
        """Get agent by ID."""
        return Agent.query.get(agent_id)
    
    @staticmethod
    def get_by_creator(user_id):
        """Get all agents created by a specific user."""
        return Agent.query.filter_by(created_by=user_id).all()
    
    def update_performance_metrics(self, metrics):
        """Update agent performance metrics."""
        current_metrics = self.performance_metrics or {}
        current_metrics.update(metrics)
        self.performance_metrics = current_metrics
        db.session.commit()
    
    def update_status(self, new_status):
        """Update agent status."""
        valid_statuses = ['inactive', 'active', 'busy', 'error']
        if new_status not in valid_statuses:
            raise ValueError(f'Invalid status. Must be one of: {", ".join(valid_statuses)}')
        self.status = new_status
        db.session.commit()
    
    def add_skill(self, skill):
        """Add a new skill to the agent."""
        current_skills = self.skills or []
        if skill not in current_skills:
            current_skills.append(skill)
            self.skills = current_skills
            db.session.commit()
    
    def remove_skill(self, skill):
        """Remove a skill from the agent."""
        current_skills = self.skills or []
        if skill in current_skills:
            current_skills.remove(skill)
            self.skills = current_skills
            db.session.commit()
