import sys
import pyaudio
import wave
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QComboBox, QDialog

class RecorderWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set parameters for recording
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.CHUNK = 1024
        self.RECORD_SECONDS = 5
        self.WAVE_OUTPUT_FILENAME = "output.wav"

        # Initialize PyAudio object
        self.audio = pyaudio.PyAudio()

        # Create combo box for input device selection
        self.deviceComboBox = QComboBox(self)
        self.deviceComboBox.setGeometry(100, 50, 200, 30)
        self.list_input_devices()

        # Create "Record" button
        self.recordBtn = QPushButton("Record", self)
        self.recordBtn.setGeometry(100, 100, 100, 30)
        self.recordBtn.clicked.connect(self.record)

        # Create label for status messages
        self.statusLabel = QLabel("Select input device and click 'Record' to begin recording.", self)
        self.statusLabel.setGeometry(100, 150, 300, 30)

        # Set window parameters
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("Audio Recorder")

    def list_input_devices(self):
        # Get the list of available input devices
        device_count = self.audio.get_device_count()
        for i in range(device_count):
            device_info = self.audio.get_device_info_by_index(i)
            if device_info['maxInputChannels'] > 0:
                self.deviceComboBox.addItem(device_info['name'], i)

    def record(self):
        # Get selected input device index
        selected_device_index = self.deviceComboBox.currentData()

        # Open stream for recording
        self.stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                                      rate=self.RATE, input=True,
                                      input_device_index=selected_device_index,
                                      frames_per_buffer=self.CHUNK)

        # Update status message
        self.statusLabel.setText("Recording...")

        # Initialize list to store frames
        self.frames = []

        # Record for the specified number of seconds
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = self.stream.read(self.CHUNK)
            self.frames.append(data)

        # Update status message
        self.statusLabel.setText("Recording finished.")

        # Stop stream and close PyAudio object
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

        # Save recorded audio as WAV file
        wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

#if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    recorder = RecorderWindow()
#    recorder.show()
#    sys.exit(app.exec_())

#show windows
RecorderWindow_render = RecorderWindow()
RecorderWindow_render.show()

