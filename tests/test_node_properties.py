```python
import unittest
from src.node_editor.node_properties import NodeProperties

class TestNodeProperties(unittest.TestCase):

    def setUp(self):
        self.node_properties = NodeProperties()

    def test_add_property(self):
        self.node_properties.add_property('node1', 'property1', 'value1')
        self.assertEqual(self.node_properties.get_property('node1', 'property1'), 'value1')

    def test_modify_property(self):
        self.node_properties.add_property('node1', 'property1', 'value1')
        self.node_properties.modify_property('node1', 'property1', 'value2')
        self.assertEqual(self.node_properties.get_property('node1', 'property1'), 'value2')

    def test_delete_property(self):
        self.node_properties.add_property('node1', 'property1', 'value1')
        self.node_properties.delete_property('node1', 'property1')
        self.assertIsNone(self.node_properties.get_property('node1', 'property1'))

    def test_get_property(self):
        self.node_properties.add_property('node1', 'property1', 'value1')
        self.assertEqual(self.node_properties.get_property('node1', 'property1'), 'value1')

    def test_get_all_properties(self):
        self.node_properties.add_property('node1', 'property1', 'value1')
        self.node_properties.add_property('node1', 'property2', 'value2')
        self.assertEqual(self.node_properties.get_all_properties('node1'), {'property1': 'value1', 'property2': 'value2'})

if __name__ == '__main__':
    unittest.main()
```