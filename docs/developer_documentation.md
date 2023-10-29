# Developer Documentation

## Overview

This project is a Node Editor and Execution Engine developed in Python. It is designed to be modular, easily extendible, and can support a wide variety of nodes including but not limited to computational tasks, decision trees, and data manipulation.

## Getting Started

To get started with the development, clone the repository and install the necessary dependencies.

## Project Structure

The project is structured as follows:

- `src/`: Contains the source code for the Node Editor and Execution Engine.
- `tests/`: Contains unit tests for the various modules.
- `docs/`: Contains the user and developer documentation.
- `demos/`: Contains a demo showcasing various types of nodes and a sample execution.

## Source Code

The source code is divided into three main parts: the Node Editor, the Execution Engine, and the Extendibility modules.

### Node Editor

The Node Editor is responsible for providing an intuitive graphical user interface for adding, deleting, and connecting nodes. It supports drag-and-drop operations for nodes and connections, allows defining and modifying properties for each node through the GUI, and can save and load node configurations.

- `gui_interface.py`: Handles the GUI interface for the Node Editor.
- `drag_and_drop.py`: Implements the drag-and-drop functionality.
- `node_properties.py`: Manages the properties of each node.
- `serialization.py`: Handles the saving and loading of node configurations.

### Execution Engine

The Execution Engine is responsible for executing a graph of nodes in real-time. It uses a plug-and-play approach for adding new types of nodes, has a comprehensive error handling and logging mechanism, facilitates data flow between connected nodes, and can handle multi-threading for computationally intensive tasks.

- `run_time_execution.py`: Handles the real-time execution of the node graph.
- `modular_architecture.py`: Implements the modular architecture of the Execution Engine.
- `error_handling.py`: Manages error handling and logging.
- `data_flow.py`: Facilitates data flow between nodes.
- `threading.py`: Handles multi-threading.

### Extendibility

The Extendibility modules provide an API for creating custom nodes and ensure that newer versions can run older node graphs.

- `custom_nodes.py`: Provides an API for creating custom nodes.
- `version_compatibility.py`: Ensures version compatibility.

## Unit Tests

Unit tests are provided for each module and aim to cover at least 80% of the code. The tests are located in the `tests/` directory.

## Documentation

User and developer documentation is provided in the `docs/` directory.

## Demo

A demo showcasing various types of nodes and a sample execution is provided in the `demos/` directory.

## Contributing

Contributions are welcome. Please follow the standard fork -> patch -> pull request workflow.

## License

This project is licensed under the MIT License.