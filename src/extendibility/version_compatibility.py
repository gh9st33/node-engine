```python
import json
from src.node_editor.serialization import load_graph

class VersionCompatibility:
    def __init__(self):
        self.versions = {}

    def register_version(self, version, node_types):
        self.versions[version] = node_types

    def is_compatible(self, graph_file, version):
        graph = load_graph(graph_file)
        node_types = self.versions.get(version, None)

        if not node_types:
            return False

        for node in graph.nodes:
            if node.type not in node_types:
                return False

        return True

    def convert_to_latest(self, graph_file, old_version):
        if not self.is_compatible(graph_file, old_version):
            raise Exception(f"Graph file is not compatible with version {old_version}")

        graph = load_graph(graph_file)
        new_version = max(self.versions.keys())
        new_node_types = self.versions[new_version]

        for node in graph.nodes:
            if node.type not in new_node_types:
                raise Exception(f"Node type {node.type} is not supported in version {new_version}")

        return graph
```