```python
import sys
sys.path.append("../src")

from node_editor.gui_interface import GUIInterface
from node_editor.node_properties import NodeProperties
from execution_engine.run_time_execution import RunTimeExecution
from extendibility.custom_nodes import CustomNodes

def main():
    # Initialize the GUI interface
    gui = GUIInterface()

    # Create some nodes
    node1 = gui.create_node(NodeProperties(type="computational", properties={"operation": "add"}))
    node2 = gui.create_node(NodeProperties(type="decision", properties={"condition": "x > 0"}))
    node3 = gui.create_node(NodeProperties(type="data", properties={"data": [1, 2, 3]}))

    # Connect the nodes
    gui.connect_nodes(node1, node2)
    gui.connect_nodes(node2, node3)

    # Save the node configuration
    gui.save_configuration("demo_config.json")

    # Load the node configuration
    gui.load_configuration("demo_config.json")

    # Run the graph
    execution_engine = RunTimeExecution(gui.graph)
    execution_engine.run()

    # Create a custom node
    custom_node = CustomNodes.create_node("custom", {"custom_property": "value"})
    gui.add_node(custom_node)

    # Run the graph with the custom node
    execution_engine.run()

if __name__ == "__main__":
    main()
```