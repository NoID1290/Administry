import sys
import svctaskk
import ckbuildV
import moduleBoot
import pathDir
#import bootScreen
#from ckGpu import GPUname
from admtools_W import btnSelect
from hwabt_W import exec__hw0

from PyQt5.QtWidgets import (
    QMainWindow, QPushButton, QHBoxLayout, QLabel,
    QStatusBar, QWidget, QToolBar, QDesktopWidget, QApplication
)
from PyQt5.QtGui import QIcon

class main_Win0(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(ckbuildV.finalTitle) # Main Title
        self.setWindowIcon(QIcon(pathDir.adm_ico)) # Main Window Icon
        self.setGeometry(100, 100, 550, 380) # Main Window Resolution
        self.setFixedSize(self.size()) # Disable resize & maximize

        # Center the main window
        self.center()

        # Button setup
        mainBtn = [
            ("Restart Windows GUI", svctaskk.WIN_GUI_KILL, (50, 50)),
            ("Restart Elgato Stream Deck", svctaskk.ELGATO_STREAMDECK_KILL, (50, 120)),
            ("About PC", self.showAboutPC, (50, 190)),
            ("Video Converter", moduleBoot.runningVconverter, (300, 260)),
            ("Cipher Password Generator", None, (300, 50)), # waiting for module completion
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
        copyright_widget_layout.addWidget(QLabel(ckbuildV.copyrighttext + ckbuildV.build))

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

    # Define admTools method
    def admTools(self):
        self.admin_tools_window = btnSelect()
        self.admin_tools_window.show()

    # Define showAboutPC method
    def showAboutPC(self):
        self.hw_0 = exec__hw0(QApplication.instance())

# Application entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = main_Win0()
    mainWin.show()
    sys.exit(app.exec_())
