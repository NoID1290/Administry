## ADMINISTRY GUI ALPHA ##
## by NoID1290 ##



import sys
import subprocess
import win32api
import win32con
import platform
import svctaskk
import version
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

# FileVer-Check
ver = f"{version.major}.{version.minor}.{version.build}"
maintitle = "Administry " #added tab for title space
finalTitle = maintitle + ver  

# MainWindows-Setup
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle(finalTitle)

# Button-Set
button1 = QPushButton("Restart Windows GUI", window)
button1.setGeometry(50, 50, 200, 50)
button1.setEnabled(True)
button1.clicked.connect(svctaskk.WIN_GUI_KILL)

button2 = QPushButton("Bouton 2", window)
button2.setGeometry(50, 120, 200, 50)
button2.setEnabled(False)

button3 = QPushButton("Bouton 3", window)
button3.setGeometry(50, 190, 200, 50)
button3.setEnabled(False)

# MainWindows-Rendering
window.setGeometry(100, 100, 300, 300)
window.show()

# START LOOP
sys.exit(app.exec_())

