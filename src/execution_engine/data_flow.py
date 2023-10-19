```python
from src.node_editor.node_properties import Node
from src.execution_engine.error_handling import ErrorTypes

class DataFlow:
    def __init__(self):
        self.data = {}

    def set_data(self, node_id, data):
        self.data[node_id] = data

    def get_data(self, node_id):
        return self.data.get(node_id, None)

    def transfer_data(self, from_node: Node, to_node: Node):
        if not isinstance(from_node, Node) or not isinstance(to_node, Node):
            raise TypeError(ErrorTypes.INVALID_NODE_TYPE)

        if from_node.id not in self.data:
            raise ValueError(ErrorTypes.DATA_NOT_FOUND)

        self.set_data(to_node.id, self.get_data(from_node.id))
```