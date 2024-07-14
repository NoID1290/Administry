import sys
import svctaskk
import buildVerCk
import moduleBoot
import pathDir
import ckHardware
from ckHardware import GPUname, get_cpu_info
from admtoolsW import btnSelect

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
        self.buildV = QLabel(buildVerCk.ver, self)  # Replace with buildVerCk.ver
        self.buildV.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        self.buildV.setStyleSheet("font-size: 14px; font-style: bold; color: #BBBBBB;")
        
        layout.addWidget(self.buildV)
        
        self.setLayout(layout)
        
        # Center the welcome screen
        self.center()

    def center(self): #Center to monitor
        screen = QDesktopWidget().availableGeometry().center()
        fg = self.frameGeometry()
        fg.moveCenter(screen)
        self.move(fg.topLeft())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(buildVerCk.finalTitle)
        self.setWindowIcon(QIcon(pathDir.adm_ico))
        self.setGeometry(100, 100, 550, 380)
        self.setFixedSize(self.size()) # Disable resize & maximize

        # Center the main window
        self.center()

        # Button setup
        mainBtn = [
            ("Restart Windows GUI", svctaskk.WIN_GUI_KILL, (50, 50)),
            ("Restart Steam", svctaskk.STEAM_VALVE_KILL, (50, 120)),
            ("Restart Elgato Stream Deck", svctaskk.ELGATO_STREAMDECK_KILL, (50, 190)),
            ("Video Converter", moduleBoot.runningVconverter, (300, 260)),
            ("Cipher Password Generator", None, (300, 50)), # waiting for module completed
            ("Administration Tools", self.admTools, (300, 120)),
            ("Audio Recording", moduleBoot.runningAudioR, (300, 190)),
            ("Restart HWINFO64", svctaskk.HWINFO64_KILL, (50, 260)),
        ]

        for text, func, pos in mainBtn:
            btn = QPushButton(text, self)
            btn.setGeometry(*pos, 200, 50) # All buttons geometry
            btn.setEnabled(func is not None)
            if func:
                btn.clicked.connect(func)

        # Copyright bar
        copyright_widget = QWidget()
        copyright_widget_layout = QHBoxLayout()
        copyright_widget.setLayout(copyright_widget_layout)
        build = f"| {buildVerCk.major}{buildVerCk.minor}{buildVerCk.build}"
        copyrighttext = f"| {buildVerCk.copyright}"
        copyright_widget_layout.addWidget(QLabel(copyrighttext + build + " " + GPUname))

        # Status bar
        status_bar = QStatusBar()
        status_bar.addWidget(copyright_widget)
        self.setStatusBar(status_bar)

        # Toolbar
        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setDisabled(True) #Disable/Enable access to toolbar
        toolbar.setWindowTitle("Hide toolbar")
        toolbar.setToolTip("Need Help?") #Easter Egg

        for action in ["Options", "Help?", "About"]:
            toolbar.addAction(action)
        self.addToolBar(toolbar)

    def center(self): #Center to monitor
        screen = QDesktopWidget().availableGeometry().center()
        fg = self.frameGeometry()
        fg.moveCenter(screen)
        self.move(fg.topLeft())

    # Define Qapp
    def admTools(self):
        self.admin_tools_window = btnSelect()
        self.admin_tools_window.show()

def main():
    app = QApplication(sys.argv)

    # Create and show the welcome screen
    welcome_screen = WelcomeScreen()
    welcome_screen.show()
    
    # Force the application to process all pending events (Loading)
    app.processEvents()
    
    # Time Sleep
    import time
    time.sleep(2)
    
    # Create and show the main window
    main_window = MainWindow()
    main_window.show()
    
    # Close the welcome screen
    welcome_screen.close()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
