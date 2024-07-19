import buildVerCk
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QHBoxLayout, QLabel,
    QStatusBar, QWidget, QToolBar, QVBoxLayout, QGraphicsDropShadowEffect,
    QDesktopWidget
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer  # Importing Qt for alignment constants


class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(400, 300)
        self.setStyleSheet("""
            background-color: qlineargradient(
                spread:pad, x1:0, y1:0, x2:1, y2:1, 
                stop:0 #3a3a3a, stop:1 #2E2E2E
            );
            color: white;
            border-radius: 10px;
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Add title
        self.label = QLabel("Administry", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 26px; font-weight: bold; font-family: 'Helvetica';")
        
        # Drop shadow effect for title
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setColor(Qt.black)
        shadow.setOffset(2, 2)
        self.label.setGraphicsEffect(shadow)
        
        layout.addWidget(self.label)
        
        # Add build version
        self.buildV = QLabel(buildVerCk.ver, self) 
        self.buildV.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        self.buildV.setStyleSheet("font-size: 14px; font-style: bold; color: #BBBBBB;")
        
        layout.addWidget(self.buildV)
        
        self.setLayout(layout)
        
        # Center the welcome screen
        self.center()

    def center(self): # Center to monitor
        screen = QDesktopWidget().availableGeometry().center()
        fg = self.frameGeometry()
        fg.moveCenter(screen)
        self.move(fg.topLeft())