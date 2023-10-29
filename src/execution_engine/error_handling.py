```python
import logging

class ErrorTypes:
    NODE_ERROR = "NODE_ERROR"
    GRAPH_ERROR = "GRAPH_ERROR"
    EXECUTION_ERROR = "EXECUTION_ERROR"
    DATA_ERROR = "DATA_ERROR"

class ErrorHandler:
    def __init__(self):
        self.logger = logging.getLogger('NodeExecutionEngine')
        self.logger.setLevel(logging.ERROR)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)

    def log_error(self, error_type, node_id=None, message=None):
        if error_type == ErrorTypes.NODE_ERROR:
            self.logger.error(f"Node Error at Node ID: {node_id}. {message}")
        elif error_type == ErrorTypes.GRAPH_ERROR:
            self.logger.error(f"Graph Error. {message}")
        elif error_type == ErrorTypes.EXECUTION_ERROR:
            self.logger.error(f"Execution Error. {message}")
        elif error_type == ErrorTypes.DATA_ERROR:
            self.logger.error(f"Data Error at Node ID: {node_id}. {message}")
        else:
            self.logger.error("Unknown Error. Please check the system.")

    def handle_error(self, error_type, node_id=None, message=None):
        self.log_error(error_type, node_id, message)
        # Add additional error handling logic here if needed
```
