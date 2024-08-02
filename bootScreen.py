
import ckbuildV
import pathDir

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QGraphicsDropShadowEffect, QDesktopWidget
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt


class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(400, 300)
        self.setStyleSheet("""
            background-color: qlineargradient(
                spread:pad, x1:0, y1:0, x2:1, y2:1, 
                stop:0 #247BA0, stop:1 #FFFFB5
            );
            color: white;
            border-radius: 10px;
        """)
        
        layout = QVBoxLayout()
        
        # Load and set the PNG image
        pixmap = QPixmap(pathDir.adm_img)  # Replace with the path to your image
        self.image_label = QLabel(self)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)
        
        # Add build version
        self.buildV = QLabel(ckbuildV.ver, self) 
        self.buildV.setAlignment(Qt.AlignBottom | Qt.AlignCenter)
        self.buildV.setStyleSheet("font-size: 18px; font-style: bold; color: #FFFFB5;")
        
       
        
        layout.addWidget(self.image_label)
        layout.addWidget(self.buildV)
        
        self.setLayout(layout)
        
        # Center the welcome screen
        self.center()
    def center(self): # Center to monitor
        screen = QDesktopWidget().availableGeometry().center()
        fg = self.frameGeometry()
        fg.moveCenter(screen)
        self.move(fg.topLeft())


