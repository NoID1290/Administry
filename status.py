import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer

class StatusBox(QWidget):
    def __init__(self):
        super().__init__()
        
        # create label for status text
        self.status_label = QLabel("Status: Idle")
        
        # add label to layout
        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        self.setLayout(layout)
        
        # create timer to update status
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_status)
        self.timer.start(1000) # update every 1 second
        
    def update_status(self):
        # call your function to get the current status text
        status_text = get_status_text()
        self.status_label.setText(f"Status: {status_text}")

def get_status_text():
    # replace this function with your own function to get the current status text
    # for this example, we will just return a random number
    import random
    return str(random.randint(0, 100))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    status_box = StatusBox()
    status_box.show()
    sys.exit(app.exec_())
