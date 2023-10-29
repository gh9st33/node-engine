```python
import unittest
from src.node_editor.serialization import Serialization
from src.node_editor.node_properties import Node

class TestSerialization(unittest.TestCase):

    def setUp(self):
        self.node1 = Node("Node1", "Compute", {"input1": 5, "input2": 10}, {"output": 15})
        self.node2 = Node("Node2", "Decision", {"condition": True}, {"result": "Yes"})
        self.serialization = Serialization()

    def test_save_node(self):
        self.serialization.save_node(self.node1)
        self.assertTrue(self.serialization.node_exists(self.node1.id))

    def test_load_node(self):
        self.serialization.save_node(self.node2)
        loaded_node = self.serialization.load_node(self.node2.id)
        self.assertEqual(loaded_node.id, self.node2.id)
        self.assertEqual(loaded_node.type, self.node2.type)
        self.assertEqual(loaded_node.inputs, self.node2.inputs)
        self.assertEqual(loaded_node.outputs, self.node2.outputs)

    def test_delete_node(self):
        self.serialization.save_node(self.node1)
        self.serialization.delete_node(self.node1.id)
        self.assertFalse(self.serialization.node_exists(self.node1.id))

if __name__ == '__main__':
    unittest.main()
```