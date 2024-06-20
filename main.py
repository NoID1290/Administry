import sys
import os
import platform
import subprocess
import win32api
import win32con
import svctaskk
import buildInfo
import buildVerCk
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QLabel, QStatusBar, QWidget, QToolBar
from PyQt5.QtGui import QIcon
from passAlgoCI import enc0
from audioRecorder import RecorderWindow  # Ensure recorder.py is in the same directory or in PYTHONPATH
# from ffconverter import STREAM_CONVERTER_FULL  # Uncomment when ffconverter is ready

# MainWindows-Setup
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle(buildVerCk.finalTitle)
window.setWindowIcon(QIcon("administryIco.ico"))

# FFConverter-Instance
def runningVconverter():
    print("Starting video converter...")
    import ffconverter  # Ensure ffconverter is in your PYTHONPATH
    print("Program closed by video converter.")
    # sys.exit()

# AudioRecorder-Instance
def runningAudioR():
    print("Starting audio recording module...")
    recorder = RecorderWindow()
    recorder.exec_()  # Run the dialog window as modal
    # sys.exit()

# Button-Set
svckill_WinGUI_btn = QPushButton("Restart Windows GUI", window)
svckill_WinGUI_btn.setGeometry(50, 50, 200, 50)
svckill_WinGUI_btn.setEnabled(True)
svckill_WinGUI_btn.clicked.connect(svctaskk.WIN_GUI_KILL)

svckill_steam_btn = QPushButton("Restart Steam", window)
svckill_steam_btn.setGeometry(50, 120, 200, 50)
svckill_steam_btn.setEnabled(True)
svckill_steam_btn.clicked.connect(svctaskk.STEAM_VALVE_KILL)

svckill_streamdeck_btn = QPushButton("Restart Elgato Stream Deck", window)
svckill_streamdeck_btn.setGeometry(50, 190, 200, 50)
svckill_streamdeck_btn.setEnabled(True)
svckill_streamdeck_btn.clicked.connect(svctaskk.ELGATO_STREAMDECK_KILL)

vConverter_btn = QPushButton("Video Converter", window)
vConverter_btn.setGeometry(50, 260, 200, 50)
vConverter_btn.setEnabled(True)
vConverter_btn.clicked.connect(runningVconverter)

enc0_btn = QPushButton("Cipher Password Generator", window)
enc0_btn.setGeometry(300, 50, 200, 50)
enc0_btn.setEnabled(True)
enc0_btn.clicked.connect(enc0)

speedtest_btn = QPushButton("Speed Test", window)
speedtest_btn.setGeometry(300, 120, 200, 50)
speedtest_btn.setEnabled(False)  # waiting module completed
# speedtest_btn.clicked.connect()  # waiting module completed

audioRecording_btn = QPushButton("Audio Recording", window)
audioRecording_btn.setGeometry(300, 190, 200, 50)
audioRecording_btn.setEnabled(True)
audioRecording_btn.clicked.connect(runningAudioR)

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

# Add a toolbar to the window
toolbar = QToolBar()
toolbar.setMovable(False)
toolbar.addAction("Options")
toolbar.addAction("Help?")
toolbar.addAction("About")
window.addToolBar(toolbar)

# MainWindows-Rendering
window.setGeometry(100, 100, 550, 380)
window.show()

# START LOOP
sys.exit(app.exec_())
