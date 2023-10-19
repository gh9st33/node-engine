```python
import unittest
from src.execution_engine.modular_architecture import ModularArchitecture

class TestModularArchitecture(unittest.TestCase):

    def setUp(self):
        self.modular_architecture = ModularArchitecture()

    def test_add_node_type(self):
        node_type = "test_node"
        self.modular_architecture.add_node_type(node_type)
        self.assertIn(node_type, self.modular_architecture.node_types)

    def test_remove_node_type(self):
        node_type = "test_node"
        self.modular_architecture.add_node_type(node_type)
        self.modular_architecture.remove_node_type(node_type)
        self.assertNotIn(node_type, self.modular_architecture.node_types)

    def test_execute_node(self):
        node_type = "test_node"
        self.modular_architecture.add_node_type(node_type)
        node_id = self.modular_architecture.create_node(node_type)
        result = self.modular_architecture.execute_node(node_id)
        self.assertIsNotNone(result)

    def test_execute_graph(self):
        node_type = "test_node"
        self.modular_architecture.add_node_type(node_type)
        node_id1 = self.modular_architecture.create_node(node_type)
        node_id2 = self.modular_architecture.create_node(node_type)
        self.modular_architecture.connect_nodes(node_id1, node_id2)
        result = self.modular_architecture.execute_graph()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
```