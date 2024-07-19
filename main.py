import sys
import bootScreen
import mainWin
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
 

def main():
    app = QApplication(sys.argv)

    # Create and show the welcome screen
    welcome_screen = bootScreen.WelcomeScreen()
    welcome_screen.show()
    
    # Force the application to process all pending events (Loading)
    app.processEvents()
    
    # Time Sleep
    import time
    time.sleep(2)
    
    # Create and show the main window
    main_window = mainWin.main_Win0()
    main_window.show()
    
    # Close the welcome screen
    welcome_screen.close()
    
    # Loop

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
