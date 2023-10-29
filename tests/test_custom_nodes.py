```python
import unittest
from src.extendibility.custom_nodes import CustomNode

class TestCustomNodes(unittest.TestCase):

    def setUp(self):
        self.custom_node = CustomNode()

    def test_create_custom_node(self):
        self.custom_node.create('CustomNode1', 'CustomType', ['input1', 'input2'], ['output1'])
        self.assertEqual(self.custom_node.id, 'CustomNode1')
        self.assertEqual(self.custom_node.type, 'CustomType')
        self.assertEqual(self.custom_node.inputs, ['input1', 'input2'])
        self.assertEqual(self.custom_node.outputs, ['output1'])

    def test_modify_custom_node(self):
        self.custom_node.create('CustomNode1', 'CustomType', ['input1', 'input2'], ['output1'])
        self.custom_node.modify('CustomNode1', 'NewType', ['new_input'], ['new_output'])
        self.assertEqual(self.custom_node.id, 'CustomNode1')
        self.assertEqual(self.custom_node.type, 'NewType')
        self.assertEqual(self.custom_node.inputs, ['new_input'])
        self.assertEqual(self.custom_node.outputs, ['new_output'])

    def test_delete_custom_node(self):
        self.custom_node.create('CustomNode1', 'CustomType', ['input1', 'input2'], ['output1'])
        self.custom_node.delete('CustomNode1')
        self.assertIsNone(self.custom_node.id)
        self.assertIsNone(self.custom_node.type)
        self.assertIsNone(self.custom_node.inputs)
        self.assertIsNone(self.custom_node.outputs)

if __name__ == '__main__':
    unittest.main()
```