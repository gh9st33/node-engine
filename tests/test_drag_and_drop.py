```python
import unittest
from src.node_editor import drag_and_drop

class TestDragAndDrop(unittest.TestCase):

    def setUp(self):
        self.node_editor = drag_and_drop.NodeEditor()

    def test_drag_node(self):
        node_id = self.node_editor.add_node('Compute')
        self.node_editor.drag_node(node_id, 100, 200)
        node = self.node_editor.get_node(node_id)
        self.assertEqual(node.position, (100, 200))

    def test_drop_node(self):
        node_id = self.node_editor.add_node('Compute')
        self.node_editor.drag_node(node_id, 100, 200)
        self.node_editor.drop_node(node_id)
        node = self.node_editor.get_node(node_id)
        self.assertEqual(node.position, (100, 200))

    def test_drag_connection(self):
        node_id1 = self.node_editor.add_node('Compute')
        node_id2 = self.node_editor.add_node('Compute')
        connection_id = self.node_editor.add_connection(node_id1, node_id2)
        self.node_editor.drag_connection(connection_id, node_id1, node_id2)
        connection = self.node_editor.get_connection(connection_id)
        self.assertEqual(connection.nodes, (node_id1, node_id2))

    def test_drop_connection(self):
        node_id1 = self.node_editor.add_node('Compute')
        node_id2 = self.node_editor.add_node('Compute')
        connection_id = self.node_editor.add_connection(node_id1, node_id2)
        self.node_editor.drag_connection(connection_id, node_id1, node_id2)
        self.node_editor.drop_connection(connection_id)
        connection = self.node_editor.get_connection(connection_id)
        self.assertEqual(connection.nodes, (node_id1, node_id2))

if __name__ == '__main__':
    unittest.main()
```