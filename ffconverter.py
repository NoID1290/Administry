import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QInputDialog
from PyQt5.QtGui import QIcon
import subprocess

def STREAM_CONVERTER_FULL():
    class App(QWidget):
        print("Video converter started module")

        def __init__(self):
            super().__init__()
            self.title = 'Video Converter'
            self.left = 250
            self.top = 250
            self.width = 320
            self.height = 100
            self.initUI()

        def initUI(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left, self.top, self.width, self.height)

            self.label = QLabel(self)
            self.label.setText("Select a video file to convert:")
            self.label.move(10, 10)

            self.btn = QPushButton('Select File', self)
            self.btn.setToolTip('Select a video file to convert')
            self.btn.move(10, 40)
            self.btn.clicked.connect(self.openFile)

            self.show()

        def openFile(self):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()","","Video Files (*.mp4 *.avi *.mov)", options=options)
            if fileName:
                self.convertFile(fileName)

        def convertFile(self, filePath):
            fileDir = os.path.dirname(filePath)
            fileName = os.path.basename(filePath)

            codec, ok = QInputDialog.getText(self, "Codec", "Enter the output codec (e.g. h264):")
            if not ok:
                return

            bitrate, ok = QInputDialog.getInt(self, "Bitrate", "Enter the output bitrate (in kbps):", 1000)
            if not ok:
                return

            outputFileName, ok = QInputDialog.getText(self, "Output File Name", "Enter the output file name (without extension):")
            if not ok:
                return

            outputFilePath = os.path.join(fileDir, outputFileName + ".mp4")

            ffmpeg_path = os.path.join(os.getcwd(), 'module', 'bin', 'ffmpeg')
            cmd = [ffmpeg_path, '-i', filePath, '-vcodec', codec, '-b:v', str(bitrate) + 'k', '-acodec', 'mp3', outputFilePath]

            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()

            if error:
                print(error.decode('utf-8'))
                return

            print("File converted successfully!")

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec_())
