import sys
import subprocess
import win32api
import win32con
import platform
import svctaskk
import version
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QLabel, QStatusBar, QWidget, QDialog, QToolBar
from PyQt5.QtGui import QIcon
from passAlgoCI import enc0



# FileVer-Check
ver = f"{version.major}.{version.minor}.{version.build}"
maintitle = "Administry " #added tab for title space
finalTitle = maintitle + ver

# MainWindows-Setup
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle(finalTitle)
window.setWindowIcon(QIcon("administryIco.ico"))
     
       
#FFConverter-Instance
def runningVconverter():
    print("Starting video converter..." )
    import ffconverter
    print("Program closed by video converter.")
    sys.exit() 
    

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

button5 = QPushButton("Cipher Password Generator",window)
button5.setGeometry(300,50,200,50)
button5.setEnabled(True)
button5.clicked.connect(enc0)

button6 = QPushButton("Speed Test",window)
button6.setGeometry(300,120,200,50)
button6.setEnabled(False)#waiting module completed
#button6.clicked.connect()#waiting module completed


# Copyright bar
copyright_widget = QWidget()
copyright_widget_layout = QHBoxLayout()
copyright_widget.setLayout(copyright_widget_layout)
build = f"| {version.major}{version.minor}{version.build}"
copyrighttext = "© 2021-2023 NoID1290. All rights reserved. "
copyright_widget_layout.addWidget(QLabel(copyrighttext+build))

# Status bar
status_bar = QStatusBar()
status_bar.addWidget(copyright_widget)
window.setStatusBar(status_bar)

# MainWindows-Rendering
window.setGeometry(100, 100, 550, 380)
window.show()


# Add a toolbar to the window
toolbar = QToolBar()
toolbar.setMovable(False)
toolbar.addAction("Option")
toolbar.addAction("Help")
window.addToolBar(toolbar)

# START LOOP
sys.exit(app.exec_())
