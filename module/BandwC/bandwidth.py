import sys
import speedtest
from PyQt5.QtCore import QThread, pyqtSignal, QObject, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class SpeedTestWorker(QObject):
    progress_update = pyqtSignal(str)
    result_ready = pyqtSignal(str)

    def run_speed_test(self):
        # Create a speedtest client
        client = speedtest.Speedtest()

        # Get the best server
        self.progress_update.emit('Finding the best server...')
        client.get_best_server()

        # Perform the speed test
        self.progress_update.emit('Running speed test...')
        download_speed = client.download() / 10**6  # Convert to Mbps
        upload_speed = client.upload() / 10**6  # Convert to Mbps

        # Emit the final results
        self.result_ready.emit(f'Download Speed: {download_speed:.2f} Mbps\n'
                               f'Upload Speed: {upload_speed:.2f} Mbps')

class SpeedTestApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Speed Test')
        self.setGeometry(300, 300, 300, 150)

        self.label = QLabel(self)
        self.button = QPushButton('Run Speed Test', self)
        self.button.clicked.connect(self.run_speed_test)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.worker = SpeedTestWorker()
        self.thread = QThread()
        self.worker.moveToThread(self.thread)

        self.worker.progress_update.connect(self.update_progress)
        self.worker.result_ready.connect(self.display_results)

        self.thread.started.connect(self.worker.run_speed_test)

    def run_speed_test(self):
        self.label.setText('Running speed test...')
        self.button.setEnabled(False)
        self.thread.start()

    def update_progress(self, progress):
        self.label.setText(progress)

    def display_results(self, results):
        self.label.setText(results)
        self.button.setEnabled(True)
        self.thread.quit()
        self.thread.wait()

    def closeEvent(self, event):
        if self.thread.isRunning():
            self.thread.quit()
            self.thread.wait()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpeedTestApp()
    window.show()
    sys.exit(app.exec_())