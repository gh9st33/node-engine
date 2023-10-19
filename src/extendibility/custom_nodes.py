```python
from src.node_editor.node_properties import Node

class CustomNode(Node):
    def __init__(self, node_id, node_type, properties):
        super().__init__(node_id, node_type)
        self.properties = properties

    def add_property(self, property_name, property_value):
        self.properties[property_name] = property_value

    def remove_property(self, property_name):
        if property_name in self.properties:
            del self.properties[property_name]

    def get_property(self, property_name):
        return self.properties.get(property_name, None)

    def set_property(self, property_name, property_value):
        self.properties[property_name] = property_value

    def execute(self):
        raise NotImplementedError("Custom nodes must implement the execute method")

class ComputationalNode(CustomNode):
    def __init__(self, node_id, properties, computation):
        super().__init__(node_id, "computational", properties)
        self.computation = computation

    def execute(self):
        return self.computation(self.properties)

class DecisionNode(CustomNode):
    def __init__(self, node_id, properties, decision):
        super().__init__(node_id, "decision", properties)
        self.decision = decision

    def execute(self):
        return self.decision(self.properties)

class DataManipulationNode(CustomNode):
    def __init__(self, node_id, properties, manipulation):
        super().__init__(node_id, "data_manipulation", properties)
        self.manipulation = manipulation

    def execute(self):
        return self.manipulation(self.properties)
```