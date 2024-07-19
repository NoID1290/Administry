import sys
import bootScreen
import mainWin
import time
from PyQt5.QtWidgets import QApplication

 

def main():
    app = QApplication(sys.argv)

    # Create and show the welcome screen
    welcome_screen = bootScreen.WelcomeScreen()
    welcome_screen.show()
    
    # Force the application to process all pending events (Loading)
    app.processEvents()
    
    # Time Sleep
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
