```python
import unittest
from src.execution_engine.data_flow import DataFlow
from src.node_editor.node_properties import Node

class TestDataFlow(unittest.TestCase):

    def setUp(self):
        self.data_flow = DataFlow()
        self.node1 = Node(node_id=1, node_type='compute', properties={'value': 10})
        self.node2 = Node(node_id=2, node_type='compute', properties={'value': 20})
        self.node3 = Node(node_id=3, node_type='compute', properties={'value': 30})

    def test_add_node(self):
        self.data_flow.add_node(self.node1)
        self.assertIn(self.node1, self.data_flow.nodes)

    def test_remove_node(self):
        self.data_flow.add_node(self.node1)
        self.data_flow.remove_node(self.node1)
        self.assertNotIn(self.node1, self.data_flow.nodes)

    def test_connect_nodes(self):
        self.data_flow.add_node(self.node1)
        self.data_flow.add_node(self.node2)
        self.data_flow.connect_nodes(self.node1, self.node2)
        self.assertIn(self.node2, self.node1.output_connections)

    def test_disconnect_nodes(self):
        self.data_flow.add_node(self.node1)
        self.data_flow.add_node(self.node2)
        self.data_flow.connect_nodes(self.node1, self.node2)
        self.data_flow.disconnect_nodes(self.node1, self.node2)
        self.assertNotIn(self.node2, self.node1.output_connections)

    def test_data_flow(self):
        self.node1.output_connections.append(self.node2)
        self.node2.input_connections.append(self.node1)
        self.node2.output_connections.append(self.node3)
        self.node3.input_connections.append(self.node2)
        self.data_flow.nodes = [self.node1, self.node2, self.node3]
        self.data_flow.execute_data_flow()
        self.assertEqual(self.node3.properties['value'], 60)

if __name__ == '__main__':
    unittest.main()
```