from modular_framework import framework
from symbolic_reasoner import SymbolicReasoner
from neural_component import NeuralComponent
from feedback_loop import iterative_workflow
from explainability_dashboard import dashboard

# Register components
reasoner = SymbolicReasoner()
framework.register_module("symbolic_reasoner", reasoner)

neural = NeuralComponent()
framework.register_module("neural_component", neural)

# Sample input data
input_data = {"data": "initial input", "embeddings": []}

# Run the iterative workflow
output = iterative_workflow(input_data)

# Update and display the dashboard
dashboard.update_data(neural.process_message("test", input_data), output)
dashboard.display()
