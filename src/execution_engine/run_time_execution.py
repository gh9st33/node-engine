```python
from src.node_editor.node_properties import Node
from src.execution_engine.data_flow import DataFlow
from src.execution_engine.error_handling import ErrorHandler
from threading import Thread

class RunTimeExecution:
    def __init__(self, graph):
        self.graph = graph
        self.data_flow = DataFlow()
        self.error_handler = ErrorHandler()

    def execute_node(self, node):
        try:
            if isinstance(node, Node):
                result = node.execute()
                self.data_flow.manage_data(node, result)
            else:
                raise TypeError("Invalid node type")
        except Exception as e:
            self.error_handler.log_error(e)

    def execute_graph(self):
        for node in self.graph.nodes:
            Thread(target=self.execute_node, args=(node,)).start()
```
