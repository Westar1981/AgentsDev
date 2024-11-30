"""
Test cases for Agent Management functionality in the Multi-AI Agent Application.
"""
import unittest
from datetime import datetime
from src.app import create_app, db
from src.auth.models import User
from werkzeug.security import generate_password_hash

class TestAgentManagement(unittest.TestCase):
    """Test suite for Agent Management functionality."""
    
    def setUp(self):
        """Set up test environment before each test."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
        # Create test user
        self.test_user = User(
            email='test@example.com',
            password=generate_password_hash('password123'),
            role='user'
        )
        db.session.add(self.test_user)
        db.session.commit()
        
        # Get authentication token
        response = self.client.post('/auth/login', json={
            'email': 'test@example.com',
            'password': 'password123'
        })
        self.auth_token = response.json['access_token']
    
    def tearDown(self):
        """Clean up test environment after each test."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_create_agent(self):
        """Test creating a new agent."""
        # Test data
        agent_data = {
            'name': 'Test Agent',
            'description': 'A test AI agent',
            'skills': ['python', 'data_analysis']
        }
        
        # Make request
        response = self.client.post(
            '/agents',
            json=agent_data,
            headers={'Authorization': f'Bearer {self.auth_token}'}
        )
        
        # Assert response
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)
        self.assertEqual(response.json['name'], agent_data['name'])
        self.assertEqual(response.json['status'], 'inactive')
    
    def test_get_agent(self):
        """Test retrieving an agent."""
        # Create test agent
        agent_data = {
            'name': 'Test Agent',
            'description': 'A test AI agent',
            'skills': ['python', 'data_analysis']
        }
        create_response = self.client.post(
            '/agents',
            json=agent_data,
            headers={'Authorization': f'Bearer {self.auth_token}'}
        )
        agent_id = create_response.json['id']
        
        # Get agent
        response = self.client.get(
            f'/agents/{agent_id}',
            headers={'Authorization': f'Bearer {self.auth_token}'}
        )
        
        # Assert response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], agent_id)
        self.assertEqual(response.json['name'], agent_data['name'])
    
    def test_update_agent(self):
        """Test updating an agent."""
        # Create test agent
        agent_data = {
            'name': 'Test Agent',
            'description': 'A test AI agent',
            'skills': ['python', 'data_analysis']
        }
        create_response = self.client.post(
            '/agents',
            json=agent_data,
            headers={'Authorization': f'Bearer {self.auth_token}'}
        )
        agent_id = create_response.json['id']
        
        # Update data
        update_data = {
            'name': 'Updated Agent',
            'status': 'active'
        }
        
        # Update agent
        response = self.client.put(
            f'/agents/{agent_id}',
            json=update_data,
            headers={'Authorization': f'Bearer {self.auth_token}'}
        )
        
        # Assert response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], update_data['name'])
        self.assertEqual(response.json['status'], update_data['status'])
    
    def test_delete_agent(self):
        """Test deleting an agent."""
        # Create test agent
        agent_data = {
            'name': 'Test Agent',
            'description': 'A test AI agent',
            'skills': ['python', 'data_analysis']
        }
        create_response = self.client.post(
            '/agents',
            json=agent_data,
            headers={'Authorization': f'Bearer {self.auth_token}'}
        )
        agent_id = create_response.json['id']
        
        # Delete agent
        response = self.client.delete(
            f'/agents/{agent_id}',
            headers={'Authorization': f'Bearer {self.auth_token}'}
        )
        
        # Assert response
        self.assertEqual(response.status_code, 204)
        
        # Verify agent is deleted
        get_response = self.client.get(
            f'/agents/{agent_id}',
            headers={'Authorization': f'Bearer {self.auth_token}'}
        )
        self.assertEqual(get_response.status_code, 404)
    
    def test_list_agents(self):
        """Test listing all agents for a user."""
        # Create multiple test agents
        agent_data_list = [
            {
                'name': 'Agent 1',
                'description': 'First test agent',
                'skills': ['python']
            },
            {
                'name': 'Agent 2',
                'description': 'Second test agent',
                'skills': ['data_analysis']
            }
        ]
        
        for agent_data in agent_data_list:
            self.client.post(
                '/agents',
                json=agent_data,
                headers={'Authorization': f'Bearer {self.auth_token}'}
            )
        
        # Get list of agents
        response = self.client.get(
            '/agents',
            headers={'Authorization': f'Bearer {self.auth_token}'}
        )
        
        # Assert response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), len(agent_data_list))
        self.assertEqual(response.json[0]['name'], agent_data_list[0]['name'])
        self.assertEqual(response.json[1]['name'], agent_data_list[1]['name'])

if __name__ == '__main__':
    unittest.main()
