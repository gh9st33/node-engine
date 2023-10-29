```python
import json
from src.node_editor.node_properties import Node

class Serialization:
    def __init__(self, graph):
        self.graph = graph

    def save_graph(self, filename):
        try:
            with open(filename, 'w') as file:
                json.dump(self.graph, file, default=self.node_to_dict)
            return True
        except Exception as e:
            print(f"Error saving graph: {e}")
            return False

    def load_graph(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            self.graph = self.dict_to_node(data)
            return True
        except Exception as e:
            print(f"Error loading graph: {e}")
            return False

    def node_to_dict(self, node):
        return {
            'id': node.id,
            'type': node.type,
            'properties': node.properties,
            'connections': [(conn.id, conn.type) for conn in node.connections]
        }

    def dict_to_node(self, data):
        node = Node(data['id'], data['type'], data['properties'])
        for conn in data['connections']:
            node.add_connection(Node(conn[0], conn[1]))
        return node
```