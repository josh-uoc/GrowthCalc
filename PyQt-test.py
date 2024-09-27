import sys
import random
import PySide6.QtCore
from PySide6 import QtCore, QtWidgets, QtGui

print(PySide6.__version__)
print(PySide6.QtCore.__version__)


# Widget class
class MyWidget(QtWidgets.QWidget):    # Defines a new class MyWidget, inherits from Qwidget    # Qwidget is a base class for all UI objects in PySide
    def __init__(self):
        super().__init__()    # Calls constructor of parent class (QWidget) to make sure it's set up correctly

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment = QtCore.Qt.AlignCenter)
        
        self.layout = QtWidgets.QVBoxLayout(self)    # Sets up a vertical box (VBox) layout for the widget. Will stack button and label vertically
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.shuffle)    # Connects the buttons clicked signal to the shuffle method

    @QtCore.Slot()    # Python decorator tag - Marks shuffle method as a Qt slot (wraps the functions behaviour)
    def shuffle(self):
        self.text.setText(random.choice(self.hello))    # Shuffle from hello list


# Main loop
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(400, 300)
    widget.show()

    sys.exit(app.exec())