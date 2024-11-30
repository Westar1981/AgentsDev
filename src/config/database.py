"""
Database configuration settings for the Multi-AI Agent Application.
"""
import os

class DatabaseConfig:
    """Database configuration settings."""
    # Default SQLite database for development
    DEV_DATABASE_URI = "sqlite:///dev.db"
    
    # In-memory SQLite database for testing
    TEST_DATABASE_URI = "sqlite:///:memory:"
    
    # Production database URI from environment variable
    PROD_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///prod.db")
    
    @staticmethod
    def get_database_uri(config_name):
        """Get database URI based on configuration name."""
        if config_name == 'testing':
            return DatabaseConfig.TEST_DATABASE_URI
        elif config_name == 'production':
            return DatabaseConfig.PROD_DATABASE_URI
        else:  # development or default
            return DatabaseConfig.DEV_DATABASE_URI
