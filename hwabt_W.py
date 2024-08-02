# hwabt.py
import sys
import pathDir
import admtools
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QProgressBar, QMainWindow, QScrollArea
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QThread, pyqtSignal

# Thread for long-running tasks
class WorkerThread(QThread):
    finished = pyqtSignal(dict)

    def run(self):
        # Simulate a long task if needed
        import time
        time.sleep(0)  # Simulate a delay | set to 0


        # Long-running task
        from ckGpu import GPUname  
        from ckCpu import (CPU_Name, Arch, CPU_Frequency_fiV_0, 
                           Physical_Cores, L2_Cache_Size_fiV_0, L3_Cache_Size_fiV_0)
        from ckOs import ckOS__finalV
        from psutil import virtual_memory
        

        # Collecting RAM
        memory_info = virtual_memory()

           
        #Format
        ram_0 = (f"{memory_info.total / (1024 ** 3):.2f} GB")



        # Collecting information from there and imports
        info = {
            "OS Release": ckOS__finalV,
            "GPU Name": GPUname,
            "CPU": CPU_Name,
            "CPU Architecture": Arch,
            "CPU Max Frequency": CPU_Frequency_fiV_0,
            "CPU Core(s)": Physical_Cores,
            "CPU L2 Cache": L2_Cache_Size_fiV_0,
            "CPU L3 Cache": L3_Cache_Size_fiV_0,
            "RAM": ram_0,
            

        }

        # Emit a signal when the task is done
        self.finished.emit(info)

# Loading screen
class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Loading...')
        self.setGeometry(100, 100, 300, 150)
        self.setWindowIcon(QIcon(pathDir.adm_ico))
        self.setFixedSize(self.size())

        layout = QVBoxLayout()
        self.label = QLabel('Retrieving hardware information...', self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.progress = QProgressBar(self)
        self.progress.setRange(0, 0)  # Indeterminate progress
        layout.addWidget(self.progress)

        self.setLayout(layout)

# Main window 
class HwAbt(QMainWindow):
    def __init__(self, info):
        super().__init__()
        self.info = info
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Hardware Info')
        self.setGeometry(100, 100, 600, 400)  # Increase window size
        self.setWindowIcon(QIcon(pathDir.adm_ico))

        # Create a central widget with a scroll area
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        self.setCentralWidget(scroll)

        container = QWidget()
        layout = QVBoxLayout(container)

        # Display information using a vertical layout
        for text, value in self.info.items():
            label = QLabel(f"{text}: {value}", self)
            label.setAlignment(Qt.AlignLeft)
            layout.addWidget(label)

        scroll.setWidget(container)

# Main application logic
class exec__hw0:
    def __init__(self, app):
        self.app = app
        self.loading_screen = LoadingScreen()
        self.loading_screen.show()

        # Start the worker thread
        self.worker = WorkerThread()
        self.worker.finished.connect(self.onFinished)
        self.worker.start()

    def onFinished(self, info):
        # Close the loading screen and show the main window
        self.loading_screen.close()
        self.hw_info = HwAbt(info)
        self.hw_info.show()
