import sys
import pathDir
import admtools
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QProgressBar, QMainWindow, QScrollArea, QDesktopWidget, QFrame
from PyQt5.QtGui import QIcon, QFont, QColor, QPalette, QPixmap
from PyQt5.QtCore import Qt, QThread, pyqtSignal

# Thread for long-running tasks
class WorkerThread(QThread):
    finished = pyqtSignal(dict)

    def run(self):
        import time
        time.sleep(0)  # Simulate a delay | set to 0

        # Long-running task
        from ckGpu import GPUname
        from ckCpu import (CPU_Name, Arch, CPU_Frequency_fiV_0,
                           Physical_Cores, L2_Cache_Size_fiV_0, L3_Cache_Size_fiV_0)
        from ckOs import ckOS__finalV
        from ckMb import mb_manufact0, mb_prod0

        from psutil import virtual_memory
        memory_info = virtual_memory()
        ram_0 = (f"{memory_info.total / (1024 ** 3):.2f} GB")

        info = {
            "OS Release": ckOS__finalV,
            "GPU Name": GPUname,
            "CPU": CPU_Name,
            "CPU Max Frequency": CPU_Frequency_fiV_0,
            "CPU Core(s)": Physical_Cores,
            "RAM": ram_0,
            "Motherboard Manufacturer": mb_manufact0,
            "Motherboard Model": mb_prod0,
        }

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
        self.progress.setRange(0, 0)
        layout.addWidget(self.progress)

        self.setLayout(layout)
        self.center()

    def center(self):
        screen = QDesktopWidget().availableGeometry().center()
        fg = self.frameGeometry()
        fg.moveCenter(screen)
        self.move(fg.topLeft())

# Main window
class HwAbt(QMainWindow):
    def __init__(self, info):
        super().__init__()
        self.info = info
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Hardware Info')
        self.setGeometry(100, 100, 700, 500)  # Window size
        self.setWindowIcon(QIcon(pathDir.adm_ico))

        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        self.setCentralWidget(scroll)

        container = QWidget()
        main_layout = QHBoxLayout(container)

        # Left container for categories
        left_container = QWidget()
        left_layout = QVBoxLayout(left_container)

        # Right container for details (if needed)
        right_container = QWidget()
        right_layout = QVBoxLayout(right_container)

        font = QFont("Segoe UI", 10)
        header_font = QFont("Segoe UI", 12, QFont.Bold)
        color = QColor("#34495E")
        palette = QPalette()
        palette.setColor(QPalette.WindowText, color)

        categories = {
            "Operating System": ["OS Release"],
            "Graphics": ["GPU Name"],
            "Processor": ["CPU", "CPU Max Frequency", "CPU Core(s)"],
            "Memory": ["RAM"],
            "Motherboard": ["Motherboard Manufacturer", "Motherboard Model"]
        }

        for category, keys in categories.items():
            category_label = QLabel(category, self)
            category_label.setFont(header_font)
            category_label.setAlignment(Qt.AlignLeft)
            category_label.setPalette(palette)
            left_layout.addWidget(category_label)
            left_layout.addWidget(self.create_separator())

            for key in keys:
                if key in self.info:
                    label = QLabel(f"{key}: {self.info[key]}", self)
                    label.setFont(font)
                    label.setAlignment(Qt.AlignLeft)
                    left_layout.addWidget(label)

            left_layout.addWidget(self.create_separator())

        # Add the image to the right container
        image_label = QLabel(self)
        pixmap = QPixmap(pathDir.adm_img)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(image_label)

        main_layout.addWidget(left_container)
        main_layout.addWidget(right_container)
        scroll.setWidget(container)
        self.center()

    def center(self):
        screen = QDesktopWidget().availableGeometry().center()
        fg = self.frameGeometry()
        fg.moveCenter(screen)
        self.move(fg.topLeft())

    def create_separator(self):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("color: #BDC3C7;")
        return line

# Main application logic
class exec__hw0:
    def __init__(self, app):
        self.app = app
        self.loading_screen = LoadingScreen()
        self.loading_screen.show()

        self.worker = WorkerThread()
        self.worker.finished.connect(self.onFinished)
        self.worker.start()

    def onFinished(self, info):
        self.loading_screen.close()
        self.hw_info = HwAbt(info)
        self.hw_info.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Custom palette for the application
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor("#ECF0F1"))
    palette.setColor(QPalette.WindowText, QColor("#2C3E50"))
    palette.setColor(QPalette.Base, QColor("#ECF0F1"))
    palette.setColor(QPalette.AlternateBase, QColor("#BDC3C7"))
    palette.setColor(QPalette.ToolTipBase, QColor("#E74C3C"))
    palette.setColor(QPalette.ToolTipText, QColor("#2C3E50"))
    palette.setColor(QPalette.Text, QColor("#2C3E50"))
    palette.setColor(QPalette.Button, QColor("#3498DB"))
    palette.setColor(QPalette.ButtonText, QColor("#FFFFFF"))
    palette.setColor(QPalette.BrightText, QColor("#E74C3C"))
    palette.setColor(QPalette.Highlight, QColor("#3498DB"))
    palette.setColor(QPalette.HighlightedText, QColor("#ECF0F1"))

    app.setPalette(palette)

    ex = exec__hw0(app)
    sys.exit(app.exec_())
