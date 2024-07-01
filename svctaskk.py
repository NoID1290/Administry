import subprocess
import win32api
import win32con
import winreg
import psutil
import sys
import time
import pyuac


from PyQt5.QtWidgets import QApplication,QWidget, QDialog, QLabel, QVBoxLayout, QPushButton, QStatusBar, QTextEdit
from PyQt5.QtCore import QTimer
from ckUac import uac







def WIN_GUI_KILL():
    
    print("Waiting for user input...")
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
            return
    
    elif ret == win32con.IDCANCEL:
        print("Operation cancelled by user.")
        return
    
def ELGATO_STREAMDECK_KILL():

    ret = win32api.MessageBox(0, "Restart Elgato Stream Deck?", "Warning", win32con.MB_OKCANCEL)
    
    if ret == win32con.IDOK:
        # checking if Elgato Stream Deck instance is running
        service_name = "StreamDeck.exe"
        service_running = False
        for proc in psutil.process_iter(['name']):
            if proc.info['name'].lower() == service_name.lower():
                service_running = True
                break
        
        if service_running:
            # read value key for Elgato StreamDeck installation path
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Elgato Systems GmbH\StreamDeck (Setup)")
            value = winreg.QueryValueEx(key, "installDir")
            elgato_value_path = value[0]
            print("Installation path found!", elgato_value_path)
            
            subprocess.run("taskkill /f /im StreamDeck.exe", shell=True)
            print("Killing Elgato Stream Deck service...")

            print("Waiting to Elgato shutting down...")
            time.sleep(3)
            
            
            subprocess.Popen([f"{elgato_value_path}\\StreamDeck.exe"])
            print("Operation completed!")
            
        else:
            print(f"{service_name} is not running.")
            win32api.MessageBox(0, "Elgato Stream Deck is not running. This tool is intended to use only if the application is running.", "Warning", win32con.MB_ICONWARNING)
            return
    
    elif ret == win32con.IDCANCEL:
        print("Operation cancelled by user.")
        return
    


def HWINFO64_KILL():

    # Check for admin privileges
    if uac == [0]:
        ret = win32api.MessageBox(0, "Administry need to restart with administrator privilege", "Warning", win32con.MB_OKCANCEL)
        if ret == win32con.IDOK:
        # Re-run the script with admin privileges
                pyuac.runAsAdmin()
        elif ret == win32con.IDCANCEL:
            print("Operation cancelled by user.")
        return
    
    
    
    ret = win32api.MessageBox(0, "Restart HWINFO64?", "Warning", win32con.MB_OKCANCEL)

    if ret == win32con.IDOK:
        
    
        # looking if hwinfo64 service is running
        service_name = "HWiNFO64.EXE"
        service_running = True
        #for proc in psutil.process_iter(['name']):
            #if proc.info['name'].lower() == service_name.lower():
                #service_running = True
                #break
                
        if service_running:
                #read value in regedit for install path
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\HWiNFO64_is1")
                value = winreg.QueryValueEx(key, "Inno Setup: App Path")
                hwinfo64_value_path = value[0]
                print("Installation path found!", hwinfo64_value_path)

                #killing service
                subprocess.run("taskkill /f /im HWiNFO64.EXE", shell=True)
                print("Killing HWINFO64 service...")

                print("Waiting to HWINFO64 shutting down...")
                time.sleep(3)

                subprocess.Popen([f"{hwinfo64_value_path}\\HWiNFO64.EXE"])
                print("Operation completed!")

        else:
                print(f"{service_name} is not running.")
                win32api.MessageBox(0, "HWINFO64 is not running. This tool is intended to use only if the application is running.", "Warning", win32con.MB_ICONWARNING)
                return
     
    elif ret == win32con.IDCANCEL:
        print("Operation cancelled by user.")
        return



     

        
       





