class CommunicationHub:
    def __init__(self):
        self.agents = {}

    def register_agent(self, name, agent):
        self.agents[name] = agent

    def send_message(self, sender, receiver, message):
        if receiver in self.agents:
            return self.agents[receiver].process_message(sender, message)
        return f"Agent {receiver} not found."

class ModularFramework:
    def __init__(self):
        self.modules = {}

    def register_module(self, name, module):
        self.modules[name] = module

    def send_message(self, sender, receiver, message):
        if receiver in self.modules:
            return self.modules[receiver].process_message(sender, message)
        else:
            return f"Module {receiver} not found."

framework = ModularFramework()
