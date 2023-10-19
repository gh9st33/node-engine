```python
import unittest
from src.execution_engine.run_time_execution import RunTimeExecution
from src.node_editor.node_properties import Node

class TestRunTimeExecution(unittest.TestCase):

    def setUp(self):
        self.execution_engine = RunTimeExecution()
        self.node1 = Node(node_id=1, node_type='compute', properties={'operation': 'add', 'value': 10})
        self.node2 = Node(node_id=2, node_type='compute', properties={'operation': 'subtract', 'value': 5})
        self.node3 = Node(node_id=3, node_type='compute', properties={'operation': 'multiply', 'value': 2})

    def test_add_node(self):
        self.execution_engine.add_node(self.node1)
        self.assertIn(self.node1, self.execution_engine.nodes)

    def test_remove_node(self):
        self.execution_engine.add_node(self.node1)
        self.execution_engine.remove_node(self.node1)
        self.assertNotIn(self.node1, self.execution_engine.nodes)

    def test_connect_nodes(self):
        self.execution_engine.add_node(self.node1)
        self.execution_engine.add_node(self.node2)
        self.execution_engine.connect_nodes(self.node1, self.node2)
        self.assertIn(self.node2, self.node1.output_connections)

    def test_execute_graph(self):
        self.execution_engine.add_node(self.node1)
        self.execution_engine.add_node(self.node2)
        self.execution_engine.add_node(self.node3)
        self.execution_engine.connect_nodes(self.node1, self.node2)
        self.execution_engine.connect_nodes(self.node2, self.node3)
        result = self.execution_engine.execute_graph()
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
```