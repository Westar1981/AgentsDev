"""
Configuration settings for the Multi-AI Agent Application.
"""
from typing import Dict, Any
import os

class Config:
    """Base configuration class."""
    # Application Settings
    APP_NAME = "Multi-AI Agent System"
    DEBUG = False
    
    # Authentication Settings
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-jwt-secret-key-here")
    
    # Database Settings
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///multi_agent.db")
    
    # Agent Settings
    MAX_AGENTS = 100
    AGENT_TIMEOUT = 300  # seconds
    
    # Task Settings
    MAX_TASKS_PER_AGENT = 10
    TASK_QUEUE_SIZE = 1000
    
    # Monitoring Settings
    ENABLE_MONITORING = True
    METRICS_INTERVAL = 60  # seconds
    
    @classmethod
    def get_config(cls) -> Dict[str, Any]:
        """Return configuration as dictionary."""
        return {
            key: value for key, value in cls.__dict__.items()
            if not key.startswith('_')
        }

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    
class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    
class TestingConfig(Config):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    DATABASE_URL = "sqlite:///test.db"

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
