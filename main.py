import sys
import pyuac
import xml.etree.ElementTree as ET
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMessageBox

import bootScreen
import main_W

CONFIG_FILE = "config.xml"

class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        
        # Load the configuration
        if self.load_config_run_as_admin():
            if not pyuac.isUserAdmin():
                pyuac.runAsAdmin()
                return  # Exit current instance, will restart as admin

        if self.load_config_bootscreen():
            # Show the welcome screen if configured
            self.welcome_screen = bootScreen.WelcomeScreen()
            self.welcome_screen.show()
            # Process all pending events
            self.app.processEvents()
            # Use QTimer to avoid blocking the GUI
            QTimer.singleShot(2000, self.show_main_window)
        else:
            self.show_main_window()
        
        # Start the application loop
        sys.exit(self.app.exec_())

    def show_main_window(self):
        if hasattr(self, 'welcome_screen'):
            self.welcome_screen.close()
        # Create and show the main window
        self.main_window = main_W.main_Win0()
        self.main_window.show()

    def load_config_bootscreen(self):
        """Load bootscreen configuration from the XML file."""
        return self.load_config('bootscreen')

    def load_config_run_as_admin(self):
        """Load runAsAdmin configuration from the XML file."""
        return self.load_config('runAsAdmin')

    def load_config(self, tag):
        """Generic method to load configuration from the XML file."""
        try:
            tree = ET.parse(CONFIG_FILE)
            root = tree.getroot()
            element = root.find(tag)
            if element is not None and element.text.lower() == 'true':
                return True
            return False
        except (ET.ParseError, FileNotFoundError, AttributeError) as e:
            QMessageBox.warning(None, "Error", f"Error loading config: {e}")
            return False

if __name__ == "__main__":
    MainApp()
