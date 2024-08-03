import sys
from svctaskk import WIN_GUI_KILL, ELGATO_STREAMDECK_KILL, HWINFO64_KILL
import ckbuildV
import moduleBoot
import pathDir
from admtools_W import btnSelect
from hwabt_W import exec__hw0

from PyQt5.QtWidgets import (
    QMainWindow, QPushButton, QHBoxLayout, QLabel,
    QStatusBar, QWidget, QDesktopWidget, QApplication, QAction, QMenuBar, QMenu, QMessageBox
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import xml.etree.ElementTree as ET

class main_Win0(QMainWindow):
    CONFIG_FILE = "config.xml"

    def __init__(self):
        super().__init__()
        self.initUI()
        self.loadConfig()

    def initUI(self):
        self.setWindowTitle(ckbuildV.finalTitle)  # Main Title
        self.setWindowIcon(QIcon(pathDir.adm_ico))  # Main Window Icon
        self.setGeometry(100, 100, 550, 380)  # Main Window Resolution
        self.setFixedSize(self.size())  # Disable resize & maximize

        # Center the main window
        self.center()

        # Button setup
        mainBtn = [
            ("Restart Windows GUI", WIN_GUI_KILL, (50, 50)),
            ("Restart Elgato Stream Deck", ELGATO_STREAMDECK_KILL, (50, 120)),
            ("About PC", self.showAboutPC, (50, 190)),
            ("Video Converter", moduleBoot.runningVconverter, (300, 260)),
            ("Cipher Password Generator", None, (300, 50)),  # waiting for module completion
            ("Administration Tools", self.admTools, (300, 120)),
            ("Audio Recording", moduleBoot.runningAudioR, (300, 190)),
            ("Restart HWINFO64", HWINFO64_KILL, (50, 260)),
        ]

        for text, func, pos in mainBtn:  # All buttons functions
            btn = QPushButton(text, self)
            btn.setGeometry(*pos, 200, 40)  # All buttons geometry
            btn.setEnabled(func is not None)
            if func:
                btn.clicked.connect(func)

        # Copyright bar
        copyright_widget = QWidget()
        copyright_widget_layout = QHBoxLayout()
        copyright_widget.setLayout(copyright_widget_layout)
        copyright_widget_layout.addWidget(QLabel(ckbuildV.copyrighttext + ckbuildV.build))

        # Status bar
        status_bar = QStatusBar()
        status_bar.addWidget(copyright_widget)
        self.setStatusBar(status_bar)

        # Menu Bar
        menu_bar = self.menuBar()
        menu_bar.setDisabled(False)  # Enable / Disable menuBar

        # Creating the main menu
        file_menu = menu_bar.addMenu("File")
        options_menu = menu_bar.addMenu("Options")

        # Adding actions to the File menu
        run_action = QAction("Run", self)
        run_action.triggered.connect(self.runAction)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(run_action)
        file_menu.addAction(exit_action)

        # Adding actions to the Options menu
        self.toogle_bootscreen_action = QAction("Enable bootscreen", self, checkable=True)
        self.toogle_bootscreen_action.triggered.connect(self.saveConfig)

        option2_action = QAction("Option 2", self)
        option2_action.setEnabled(False) # Waiting for module to me completed
        option2_action.triggered.connect(self.option2Action)

        options_menu.addAction(self.toogle_bootscreen_action)
        options_menu.addAction(option2_action)

    def center(self):  # Center to monitor
        screen = QDesktopWidget().availableGeometry().center()
        fg = self.frameGeometry()
        fg.moveCenter(screen)
        self.move(fg.topLeft())

    def runAction(self):
        print("Run action triggered")

    def option2Action(self):
        print("Option 2 action triggered")

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

    def saveConfig(self):
        bootscreen = self.root.find('bootscreen')
        if bootscreen is None:
            bootscreen = ET.SubElement(self.root, "bootscreen")
        bootscreen.text = 'true' if self.toogle_bootscreen_action.isChecked() else 'false'
        self.tree.write(self.CONFIG_FILE, encoding='utf-8', xml_declaration=True)

    def admTools(self):
        self.admin_tools_window = btnSelect()
        self.admin_tools_window.show()

    def showAboutPC(self):
        self.hw_0 = exec__hw0(QApplication.instance())

# Application entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = main_Win0()
    mainWin.show()
    sys.exit(app.exec_())
