from PyQt5.QtWidgets import (
    QMainWindow, QPushButton, QHBoxLayout, QLabel,
    QStatusBar, QWidget, QDesktopWidget, QApplication, QAction, QMenuBar, QMenu, QMessageBox
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import xml.etree.ElementTree as ET
CONFIG_FILE = "config.xml"




def loadConfig(self):
    try:
        self.tree = ET.parse(self.CONFIG_FILE)
        self.root = self.tree.getroot()
        bootscreen = self.root.find('bootscreen').text == 'true'
        self.toogle_bootscreen_action.setChecked(bootscreen)
    except (ET.ParseError, FileNotFoundError, AttributeError) as e:
        QMessageBox.warning(self, "Error", f"Error loading config: {e}")
        self.root = ET.Element("config")
        self.tree = ET.ElementTree(self.root)


