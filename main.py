import sys
import bootScreen
import main_W
import time
from PyQt5.QtWidgets import QApplication, QMessageBox
import xml.etree.ElementTree as ET

CONFIG_FILE = "config.xml"

class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.welcome_screen = bootScreen.WelcomeScreen()
        self.welcome_screen.show()
        
        # Process all pending events
        self.app.processEvents()
        
        # Load the configuration
        self.loadConfig()
        
        # Create and show the main window
        self.main_window = main_W.main_Win0()
        self.main_window.show()
        
        # Close the welcome screen
        self.welcome_screen.close()
        
        # Start the application loop
        sys.exit(self.app.exec_())

    def loadConfig(self):
        try:
            tree = ET.parse(CONFIG_FILE)
            root = tree.getroot()
            bootscreen = root.find('bootscreen').text == 'true'
            if bootscreen:
                time.sleep(3)
            else:
                time.sleep(0)
        except (ET.ParseError, FileNotFoundError, AttributeError) as e:
            QMessageBox.warning(None, "Error", f"Error loading config: {e}")

if __name__ == "__main__":
    MainApp()
