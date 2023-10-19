```python
from src.node_editor.node_properties import Node

class NodeFactory:
    def __init__(self):
        self.node_classes = {}

    def register_node(self, node_type, node_class):
        if not issubclass(node_class, Node):
            raise ValueError("Invalid node class: {}".format(node_class))
        self.node_classes[node_type] = node_class

    def create_node(self, node_type, *args, **kwargs):
        if node_type not in self.node_classes:
            raise ValueError("Invalid node type: {}".format(node_type))
        return self.node_classes[node_type](*args, **kwargs)

class ExecutionEngine:
    def __init__(self, node_factory):
        self.node_factory = node_factory
        self.graph = {}

    def add_node(self, node_type, node_id, *args, **kwargs):
        node = self.node_factory.create_node(node_type, *args, **kwargs)
        self.graph[node_id] = node

    def remove_node(self, node_id):
        if node_id in self.graph:
            del self.graph[node_id]

    def connect_nodes(self, node_id1, node_id2):
        if node_id1 not in self.graph or node_id2 not in self.graph:
            raise ValueError("Invalid node ID")
        self.graph[node_id1].add_connection(self.graph[node_id2])

    def disconnect_nodes(self, node_id1, node_id2):
        if node_id1 not in self.graph or node_id2 not in self.graph:
            raise ValueError("Invalid node ID")
        self.graph[node_id1].remove_connection(self.graph[node_id2])

    def execute_graph(self):
        for node in self.graph.values():
            node.execute()
```
