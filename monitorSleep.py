import sys
import time
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer
import ctypes

# Constants from Windows API
HWND_BROADCAST = 0xFFFF
WM_SYSCOMMAND = 0x0112
SC_MONITORPOWER = 0xF170
MONITOR_OFF = 2

def force_monitor_sleep():
    # Call the SendMessageTimeout function from Windows API
    ctypes.windll.user32.SendMessageTimeoutW(
        HWND_BROADCAST, WM_SYSCOMMAND,
        SC_MONITORPOWER, MONITOR_OFF,
        0, 5000  # 5000 milliseconds timeout
    )

class CountdownDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Countdown")
        layout = QVBoxLayout(self)

        self.label = QLabel()
        layout.addWidget(self.label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_countdown)
        self.countdown_seconds = 5
        self.update_countdown()  # Initial update
        self.timer.start(1000)  # Update every second

    def update_countdown(self):
        self.label.setText(f"Turning off monitor in {self.countdown_seconds} seconds")
        self.countdown_seconds -= 1
        if self.countdown_seconds < 0:
            self.timer.stop()
            force_monitor_sleep()
            self.close()

def force_monitor_sleep():
    # Call the SendMessageTimeout function from Windows API
    ctypes.windll.user32.SendMessageTimeoutW(
        HWND_BROADCAST, WM_SYSCOMMAND,
        SC_MONITORPOWER, MONITOR_OFF,
        0, 5000  # 5000 milliseconds timeout
    )
