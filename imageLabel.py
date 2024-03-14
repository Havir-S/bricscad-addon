from PyQt5.QtWidgets import QLabel
from PyQt5 import  QtCore

class ImageLabel(QLabel):
    clicked = QtCore.pyqtSignal(str)

    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def mousePressEvent(self, event):
        self.clicked.emit(self.filename)