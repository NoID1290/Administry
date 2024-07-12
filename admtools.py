
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QHBoxLayout, QLabel,
    QStatusBar, QWidget, QToolBar, QVBoxLayout, QDialog
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer  # Importing Qt for alignment constants



    
class btnSelect(QWidget):
    def __init__(self):
        super().__init__()     
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Test Title')
        self.setGeometry(300, 300, 600, 300)

        self.show
        