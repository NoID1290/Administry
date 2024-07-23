import pathDir
import admtools
from PyQt5.QtWidgets import (
    QPushButton, QWidget
)
from PyQt5.QtGui import QIcon



    
class btnSelect(QWidget):
    def __init__(self):
        super().__init__()     
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Administration Tools')
        self.setGeometry(100, 100, 550, 380)
        self.setWindowIcon(QIcon(pathDir.adm_ico))
        self.setFixedSize(self.size()) # Disable resize & maximize


        # Adm Button setup
        admBtn = [
            ("LUAGM",admtools.luagm_access, (50, 50)),
            ("Windows Features", admtools.winFeatures_access, (50, 120)),
            ("Windows God Mode", admtools.winGodMod_access, (50, 190)),
            ("Startup Folder", admtools.startupFolder_access, (50, 260)),
            ("Refresh graphic driver", None, (300, 190)),
            ("Refresh audio driver", None, (300, 120)),
            ("Windows 10/11 switch menu context", None, (300, 50)),
        ]
        
        for text, func, pos in admBtn:
            btn = QPushButton(text, self)
            btn.setGeometry(*pos, 200, 50) # All buttons geometry
            btn.setEnabled(func is not None)
            if func:
                btn.clicked.connect(func)
                
        self.show
        