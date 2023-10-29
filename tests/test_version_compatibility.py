```python
import unittest
from src.extendibility.version_compatibility import VersionCompatibility

class TestVersionCompatibility(unittest.TestCase):

    def setUp(self):
        self.version_compatibility = VersionCompatibility()

    def test_backward_compatibility(self):
        old_version_graph = {
            'nodes': [
                {'id': 1, 'type': 'compute', 'properties': {'operation': 'add', 'value': 10}},
                {'id': 2, 'type': 'compute', 'properties': {'operation': 'multiply', 'value': 5}},
                {'id': 3, 'type': 'output', 'properties': {}}
            ],
            'connections': [
                {'from': 1, 'to': 2},
                {'from': 2, 'to': 3}
            ]
        }

        result = self.version_compatibility.run_old_version_graph(old_version_graph)
        self.assertEqual(result, 50, "Old version graph should be compatible with new version")

    def test_forward_compatibility(self):
        new_version_graph = {
            'nodes': [
                {'id': 1, 'type': 'compute', 'properties': {'operation': 'subtract', 'value': 10}},
                {'id': 2, 'type': 'compute', 'properties': {'operation': 'divide', 'value': 5}},
                {'id': 3, 'type': 'output', 'properties': {}}
            ],
            'connections': [
                {'from': 1, 'to': 2},
                {'from': 2, 'to': 3}
            ]
        }

        result = self.version_compatibility.run_new_version_graph(new_version_graph)
        self.assertEqual(result, 2, "New version graph should be compatible with old version")

if __name__ == '__main__':
    unittest.main()
```