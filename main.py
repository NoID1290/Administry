## ADMINISTRY GUI ALPHA ##
## by NoID1290 ##

import sys
import subprocess
import win32api
import win32con
import platform
import svctaskk
import version
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QLabel, QStatusBar, QWidget, QDialog
from PyQt5.QtGui import QIcon
from ffconverter import STREAM_CONVERTER_FULL

# FileVer-Check
ver = f"{version.major}.{version.minor}.{version.build}"
maintitle = "Administry " #added tab for title space
finalTitle = maintitle + ver

# MainWindows-Setup
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle(finalTitle)
window.setWindowIcon(QIcon("administryIco.ico"))

class SecondaryWindow(QDialog):
    def __init__(self):
        super().__init__()
        
        # Set the window title and size
        self.setWindowTitle('Secondary Window')
        self.setGeometry(100, 100, 400, 300)
        
        # Add a label to the window
        label = QLabel('This is a secondary window', self)
        label.move(100, 100)



def runningVconverter():
    print("Starting video converter...")
    import ffconverter
    converter = ffconverter.STREAM_CONVERTER_FULL()
    
    # Create an instance of the secondary window
    secondary_window = SecondaryWindow()
    secondary_window.exec_()








    


# Button-Set
button1 = QPushButton("Restart Windows GUI", window)
button1.setGeometry(50, 50, 200, 50)
button1.setEnabled(True)
button1.clicked.connect(svctaskk.WIN_GUI_KILL)

button2 = QPushButton("Restart Steam", window)
button2.setGeometry(50, 120, 200, 50)
button2.setEnabled(True)
button2.clicked.connect(svctaskk.STEAM_VALVE_KILL)

button3 = QPushButton("Restart Elgato Stream Deck", window)
button3.setGeometry(50, 190, 200, 50)
button3.setEnabled(True)
button3.clicked.connect(svctaskk.ELGATO_STREAMDECK_KILL)

button4 = QPushButton("Video Converter",window)
button4.setGeometry(50, 260, 200, 50)
button4.setEnabled(True)#waiting for completed code!
button4.clicked.connect(runningVconverter)


# Copyright bar
copyright_widget = QWidget()
copyright_widget_layout = QHBoxLayout()
copyright_widget.setLayout(copyright_widget_layout)
copyright_widget_layout.addWidget(
    QLabel("© 2021-2023 NoID1290. All rights reserved."))

# Status bar
status_bar = QStatusBar()
status_bar.addWidget(copyright_widget)
window.setStatusBar(status_bar)

# MainWindows-Rendering
window.setGeometry(100, 100, 300, 380)
window.show()
 


# START LOOP
sys.exit(app.exec_())
