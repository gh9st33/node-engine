```python
import unittest
from src.node_editor.gui_interface import GUIInterface

class TestGUIInterface(unittest.TestCase):

    def setUp(self):
        self.gui = GUIInterface()

    def test_add_node(self):
        initial_node_count = len(self.gui.graph.nodes)
        self.gui.add_node('ComputeNode')
        self.assertEqual(len(self.gui.graph.nodes), initial_node_count + 1)

    def test_delete_node(self):
        self.gui.add_node('ComputeNode')
        initial_node_count = len(self.gui.graph.nodes)
        self.gui.delete_node(self.gui.graph.nodes[-1].id)
        self.assertEqual(len(self.gui.graph.nodes), initial_node_count - 1)

    def test_connect_nodes(self):
        node1 = self.gui.add_node('ComputeNode')
        node2 = self.gui.add_node('ComputeNode')
        self.gui.connect_nodes(node1.id, node2.id)
        self.assertIn(node2.id, node1.output_connections)

    def test_modify_node_properties(self):
        node = self.gui.add_node('ComputeNode')
        self.gui.modify_node_properties(node.id, {'property': 'value'})
        self.assertEqual(node.properties['property'], 'value')

    def test_save_and_load_configuration(self):
        self.gui.add_node('ComputeNode')
        self.gui.save_configuration('test_config.json')
        self.gui.load_configuration('test_config.json')
        self.assertEqual(len(self.gui.graph.nodes), 1)

if __name__ == '__main__':
    unittest.main()
```