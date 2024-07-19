import ckbuildV

from PyQt5.QtWidgets import (
    QLabel, QWidget, QVBoxLayout, QGraphicsDropShadowEffect,
    QDesktopWidget
)



class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(400, 300) 
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
        self.buildV = QLabel(ckbuildV.ver, self) 
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