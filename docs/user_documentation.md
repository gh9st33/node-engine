# User Documentation

## Introduction

Welcome to our Node Editor and Execution Engine. This tool allows you to create, modify, and execute graphs of nodes for a wide variety of tasks, including computational tasks, decision trees, and data manipulation.

## Getting Started

To start the application, run the following command in your terminal:

```bash
python src/main.py
```

## Node Editor

### GUI Interface

The GUI interface allows you to add, delete, and connect nodes. To add a node, click on the "Add Node" button. To delete a node, select the node and click on the "Delete Node" button. To connect nodes, drag a line from the output of one node to the input of another node.

### Drag & Drop

You can rearrange nodes by dragging and dropping them in the GUI interface. You can also drag and drop connections between nodes.

### Node Properties

Each node has properties that can be defined and modified through the GUI. To edit a node's properties, select the node and edit the properties in the properties panel.

### Serialization

You can save and load node configurations. To save a configuration, click on the "Save" button and choose a location to save the file. To load a configuration, click on the "Load" button and select the configuration file.

## Execution Engine

### Run Time Execution

To execute a graph of nodes, click on the "Run" button. The graph will be executed in real-time, and the results will be displayed in the results panel.

### Error Handling

If there are any errors during execution, they will be logged in the error panel. You can view the details of each error by clicking on it.

### Data Flow

Data flows from the output of one node to the input of another node. The data types that can be passed between nodes are defined in the data types list.

### Threading

For computationally intensive tasks, the execution engine uses multi-threading to improve performance.

## Extendibility

### Custom Nodes

You can create custom nodes by following the instructions in the developer documentation.

### Version Compatibility

The application ensures that newer versions can run older node graphs. If you open a node graph created in an older version, it will be automatically updated to the current version.

## Conclusion

We hope this documentation helps you to use our Node Editor and Execution Engine effectively. If you have any questions or issues, please refer to the developer documentation or contact us.