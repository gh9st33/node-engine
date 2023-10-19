```python
import tkinter as tk
from .gui_interface import Node, Graph

class DragAndDrop:
    def __init__(self, canvas, node):
        self.canvas = canvas
        self.node = node
        self.drag_data = {"x": 0, "y": 0, "item": None}

    def start_drag(self, event):
        # Begin the dragging operation
        self.drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def perform_drag(self, event):
        # Compute how much the mouse has moved
        delta_x = event.x - self.drag_data["x"]
        delta_y = event.y - self.drag_data["y"]
        # Move the object the appropriate amount
        self.canvas.move(self.drag_data["item"], delta_x, delta_y)
        # Update the position in the drag data
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def end_drag(self, event):
        # Reset the drag information
        self.drag_data = {"x": 0, "y": 0, "item": None}

    def setup_draggable_node(self):
        self.canvas.tag_bind(self.node.id, "<ButtonPress-1>", self.start_drag)
        self.canvas.tag_bind(self.node.id, "<Button1-Motion>", self.perform_drag)
        self.canvas.tag_bind(self.node.id, "<ButtonRelease-1>", self.end_drag)
```