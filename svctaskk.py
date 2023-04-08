import subprocess
import win32api
import win32con
import winreg
import sys
import status
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QPushButton




def WIN_GUI_KILL():
    ret = win32api.MessageBox(0, "Restart Windows GUI Service?", "Warning", win32con.MB_OKCANCEL)
    if ret == win32con.IDOK:
        subprocess.run("taskkill /f /im explorer.exe", shell=True)
        subprocess.run("start explorer.exe", shell=True)
    
    else:
        print("Operation cancel by user")

def STEAM_VALVE_KILL():
    
    ret = win32api.MessageBox(0, "Restart Steam from Valve?", "Warning", win32con.MB_OKCANCEL)
    if ret == win32con.IDOK:()