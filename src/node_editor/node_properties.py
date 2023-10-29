```python
from PyQt5.QtWidgets import QFormLayout, QLineEdit, QDialog, QPushButton, QVBoxLayout

class NodeProperties(QDialog):
    def __init__(self, node, parent=None):
        super(NodeProperties, self).__init__(parent)
        self.node = node
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Node Properties')

        self.layout = QFormLayout(self)

        self.nameEdit = QLineEdit(self.node.name)
        self.layout.addRow("Name", self.nameEdit)

        for prop, value in self.node.properties.items():
            lineEdit = QLineEdit(value)
            self.layout.addRow(prop, lineEdit)

        self.saveButton = QPushButton('Save', self)
        self.saveButton.clicked.connect(self.saveProperties)

        vbox = QVBoxLayout()
        vbox.addLayout(self.layout)
        vbox.addWidget(self.saveButton)

        self.setLayout(vbox)

    def saveProperties(self):
        self.node.name = self.nameEdit.text()

        for i in range(self.layout.count()):
            item = self.layout.itemAt(i)
            if isinstance(item.widget(), QLineEdit):
                self.node.properties[item.widget().text()] = item.widget().text()

        self.close()
```