import sys
import os
import platform
import subprocess
import win32api
import win32con
import svctaskk
import buildInfo
import buildVerCk
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QHBoxLayout, QLabel,
    QStatusBar, QWidget, QToolBar
)
from PyQt5.QtGui import QIcon
from passAlgoCI import enc0
from audioRecorder import RecorderWindow

# Main window setup
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle(buildVerCk.finalTitle)
window.setWindowIcon(QIcon("administryIco.ico"))

# FFConverter instance
def runningVconverter():
    print("Starting video converter...")
    import ffconverter  # Ensure ffconverter is in your PYTHONPATH
    print("Program closed by video converter.")

# AudioRecorder instance
def runningAudioR():
    print("Starting audio recording module...")
    recorder = RecorderWindow()
    recorder.exec_()  # Run the dialog window as modal

# Button setup
buttons = [
    ("Restart Windows GUI", svctaskk.WIN_GUI_KILL, (50, 50)),
    ("Restart Steam", svctaskk.STEAM_VALVE_KILL, (50, 120)),
    ("Restart Elgato Stream Deck", svctaskk.ELGATO_STREAMDECK_KILL, (50, 190)),
    ("Video Converter", runningVconverter, (50, 260)),
    ("Cipher Password Generator", enc0, (300, 50)),
    ("Speed Test", None, (300, 120)),
    ("Audio Recording", runningAudioR, (300, 190)),
]
# Text function position 
for text, func, pos in buttons:
    btn = QPushButton(text, window)
    btn.setGeometry(*pos, 200, 50)
    btn.setEnabled(func is not None)
    if func:
        btn.clicked.connect(func)

# Copyright bar
copyright_widget = QWidget()
copyright_widget_layout = QHBoxLayout()
copyright_widget.setLayout(copyright_widget_layout)
build = f"| {buildInfo.major}{buildInfo.minor}{buildInfo.build}"
copyrighttext = f"| {buildInfo.copyright}"
copyright_widget_layout.addWidget(QLabel(copyrighttext + build))

# Status bar
status_bar = QStatusBar()
status_bar.addWidget(copyright_widget)
window.setStatusBar(status_bar)

# Toolbar
toolbar = QToolBar()
toolbar.setMovable(False)
for action in ["Options", "Help?", "About"]:
    toolbar.addAction(action)
window.addToolBar(toolbar)

# Main window rendering
window.setGeometry(100, 100, 550, 380)
window.show()

# Start loop
sys.exit(app.exec_())
