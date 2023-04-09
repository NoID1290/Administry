import subprocess
import win32api
import win32con
import winreg
import psutil
import sys
import status
from PyQt5.QtWidgets import QApplication,QWidget, QDialog, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import QTimer




def WIN_GUI_KILL():
    ret = win32api.MessageBox(0, "Restart Windows GUI Service?", "Warning", win32con.MB_OKCANCEL)
    if ret == win32con.IDOK:
        subprocess.run("taskkill /f /im explorer.exe", shell=True)
        subprocess.run("start explorer.exe", shell=True)
    
    else:
        print("Operation cancel by user")

def STEAM_VALVE_KILL():

    ret = win32api.MessageBox(0, "Restart Steam from Valve?", "Warning", win32con.MB_OKCANCEL)
    
    if ret == win32con.IDOK:
        # checking if Steam instance is running
        service_name = "Steam.exe"
        service_running = False
        for proc in psutil.process_iter(['name']):
            if proc.info['name'].lower() == service_name.lower():
                service_running = True
                break
        
        if service_running:
            # read value key for Steam installation path
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432NODE\Valve\Steam")
            value = winreg.QueryValueEx(key, "InstallPath")
            steam_value_path = value[0]
            print("Installation path found!", steam_value_path)
            
            subprocess.run("taskkill /f /im Steam.exe", shell=True)
            print("Killing Steam service...")
            
            subprocess.Popen([f"{steam_value_path}\\steam.exe"])
            print("Operation completed!")
            
        else:
            print(f"{service_name} is not running.")
            win32api.MessageBox(0, "Steam is not running. This tool is intended to use only if Steam is running.", "Warning", win32con.MB_ICONWARNING)
    
    elif ret == win32con.IDCANCEL:
        print("Operation cancelled by user.")
        return
            
     

        
       





