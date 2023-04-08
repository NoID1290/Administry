import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QPushButton

class StatusWindow(QDialog):
    def __init__(self, text):
        super().__init__()
        self.setWindowTitle("Status Window")
        self.setFixedSize(300, 100)
        
        self.label = QLabel(text, self)
        self.label.setFont(self.label.font().bold())
        
        self.button = QPushButton("Close", self)
        self.button.clicked.connect(self.close)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

    def set_status(self, text):
        self.label.setText(text)

def main():
    app = QApplication(sys.argv)
    status_window = StatusWindow("Task in progress...")
    status_window.show()
    status_window.set_status("Task completed.")
    app.exec_()

if __name__ == "__main__":
    main()
