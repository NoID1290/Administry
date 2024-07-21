from audioRecorder import RecorderWindow
from ffconverter import vConverterApp

# FFConverter instance
def runningVconverter():
    print("Starting video converter...")
    vRecorderffmpeg = vConverterApp()
    vRecorderffmpeg.exec_() 
    print("Video converter closed by user")
    

# AudioRecorder instance
def runningAudioR():
    print("Starting audio recording module...")
    recorder = RecorderWindow()
    recorder.exec_()
    print("Audio recorder closed by user")
