import sys
import svctaskk
import buildVerCk
import moduleBoot
import pathDir
import ckHardware
from ckHardware import GPUname, get_cpu_info

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QHBoxLayout, QLabel,
    QStatusBar, QWidget, QToolBar, QVBoxLayout
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer  # Importing Qt for alignment constants

class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #2E2E2E; color: white;")
        layout = QVBoxLayout()

        self.label = QLabel("Administry"+" "+ buildVerCk.ver, self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 24px;")
        layout.addWidget(self.label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(buildVerCk.finalTitle)
        self.setWindowIcon(QIcon(pathDir.adm_ico))

        # Button setup
        mainBtn = [
            ("Restart Windows GUI", svctaskk.WIN_GUI_KILL, (50, 50)),
            ("Restart Steam", svctaskk.STEAM_VALVE_KILL, (50, 120)),
            ("Restart Elgato Stream Deck", svctaskk.ELGATO_STREAMDECK_KILL, (50, 190)),
            ("Video Converter", moduleBoot.runningVconverter, (300, 260)),
            ("Cipher Password Generator", None, (300, 50)), # waiting for module completed
            ("Speed Test", None, (300, 120)), # waiting for module completed
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

def main():
    app = QApplication(sys.argv)

    # Create and show the welcome screen
    welcome_screen = WelcomeScreen()
    welcome_screen.show()
    
    # Force the application to process all pending events
    app.processEvents()
    
    # Time Sleep
    import time
    time.sleep(2)
    
    # Create and show the main window
    main_window = MainWindow()
    main_window.setGeometry(100, 100, 550, 380)
    main_window.show()
    
    # Close the loading screen
    welcome_screen.close()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
