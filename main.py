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
        
        # Load the configuration
        bootscreen = self.loadConfig()
        
        if bootscreen:
            # Show the welcome screen if configured
            self.welcome_screen = bootScreen.WelcomeScreen()
            self.welcome_screen.show()
            # Process all pending events
            self.app.processEvents()
            # Logo delay
            time.sleep(2)
            self.welcome_screen.close()
        
        # Create and show the main window
        self.main_window = main_W.main_Win0()
        self.main_window.show()
        
        # Start the application loop
        sys.exit(self.app.exec_())

    def loadConfig(self):
        try:
            tree = ET.parse(CONFIG_FILE)
            root = tree.getroot()
            bootscreen = root.find('bootscreen').text == 'true'
            return bootscreen
        except (ET.ParseError, FileNotFoundError, AttributeError) as e:
            QMessageBox.warning(None, "Error", f"Error loading config: {e}")
            return False

if __name__ == "__main__":
    MainApp()
