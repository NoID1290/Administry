## ADMINISTRY GUI ALPHA ##
## by NoID1290 ##



import sys
import subprocess
import win32api
import win32con
import platform
import svctaskk
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

# FILEINFO
version = "0.29.1"
maintitle = "Administry " #added tab for title space
author = "NoID1290"
finalTitle = maintitle + version   

# Création de la fenêtre principale
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle(finalTitle)

# Création des boutons
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

# Affichage de la fenêtre
window.setGeometry(100, 100, 300, 300)
window.show()

# Démarrage de la boucle principale de l'application
sys.exit(app.exec_())

