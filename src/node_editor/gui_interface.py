```python
import tkinter as tk
from node_properties import NodeProperties
from drag_and_drop import DragAndDrop

class GUIInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.node_properties = NodeProperties()
        self.drag_and_drop = DragAndDrop(self.canvas)

    def add_node(self, event):
        node_id = self.canvas.create_rectangle(50, 50, 100, 100, fill="white")
        self.node_properties.add_node(node_id)
        self.drag_and_drop.add_node(node_id)

    def delete_node(self, event):
        node_id = self.canvas.find_withtag("current")[0]
        self.canvas.delete(node_id)
        self.node_properties.delete_node(node_id)
        self.drag_and_drop.delete_node(node_id)

    def connect_nodes(self, event):
        node_id1, node_id2 = self.drag_and_drop.get_selected_nodes()
        self.canvas.create_line(self.canvas.coords(node_id1), self.canvas.coords(node_id2), fill="black")

    def run(self):
        self.root.bind("<Button-1>", self.add_node)
        self.root.bind("<Button-3>", self.delete_node)
        self.root.bind("<Double-Button-1>", self.connect_nodes)
        self.root.mainloop()

if __name__ == "__main__":
    gui = GUIInterface()
    gui.run()
```