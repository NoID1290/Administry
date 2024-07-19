import sys
import svctaskk
import buildVerCk
import moduleBoot
import pathDir
#import bootScreen
from ckHardware import GPUname, get_cpu_info
from admtoolsW import btnSelect
from monitorSleep import CountdownDialog, force_monitor_sleep  # Importing CountdownDialog and force_monitor_sleep



from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QHBoxLayout, QLabel,
    QStatusBar, QWidget, QToolBar, QVBoxLayout, QGraphicsDropShadowEffect,
    QDesktopWidget
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer  # Importing Qt for alignment constants

class main_Win0(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(buildVerCk.finalTitle) # Main Title 
        self.setWindowIcon(QIcon(pathDir.adm_ico)) # Main Windows Ico
        self.setGeometry(100, 100, 550, 380) # Main Windows Resolution
        self.setFixedSize(self.size()) # Disable resize & maximize

        # Center the main window
        self.center()

        # Button setup
        mainBtn = [
            ("Restart Windows GUI", svctaskk.WIN_GUI_KILL, (50, 50)),
            ("Restart Elgato Stream Deck", svctaskk.ELGATO_STREAMDECK_KILL, (50, 120)),
            ("Force Monitor Sleep", None, (50, 190)),  # waiting for module completed | self.show_countdown_dialog
            ("Video Converter", moduleBoot.runningVconverter, (300, 260)),
            ("Cipher Password Generator", None, (300, 50)), # waiting for module completed
            ("Administration Tools", self.admTools, (300, 120)),
            ("Audio Recording", moduleBoot.runningAudioR, (300, 190)),
            ("Restart HWINFO64", svctaskk.HWINFO64_KILL, (50, 260)),
        ]

        for text, func, pos in mainBtn: # All buttons functions
            btn = QPushButton(text, self)
            btn.setGeometry(*pos, 200, 40) # All buttons geometry
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
        toolbar.setDisabled(True) # Disable/Enable access to toolbar
        toolbar.setWindowTitle("Hide toolbar")
        toolbar.setToolTip("Need Help?") # Easter Egg

        for action in ["Options", "Help?", "About"]: 
            toolbar.addAction(action)
        self.addToolBar(toolbar)

    def center(self): # Center to monitor
        screen = QDesktopWidget().availableGeometry().center()
        fg = self.frameGeometry()
        fg.moveCenter(screen)
        self.move(fg.topLeft())

    # Define Qapp
    def admTools(self):
        self.admin_tools_window = btnSelect()
        self.admin_tools_window.show()

    def show_countdown_dialog(self):
        self.countdown_dialog = CountdownDialog()
        self.countdown_dialog.exec_()  # Show the dialog modally
        sys.exit(self.exec_()) # ?? it is work for breaking loop?