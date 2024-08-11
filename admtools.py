import os
import win32api
import win32con
import pathDir
import subprocess
from PyQt5.QtWidgets import QPushButton, QWidget
from PyQt5.QtGui import QIcon
from functools import partial


def exeXc(command, success_message):
    try:
        os.system(command)
        print(success_message)
    except Exception as e:
        print(f"An error occurred: {e}")

# Executing Windows commands        

def luagm_access():  # Local User and Group Management
    exeXc("lusrmgr.msc", "Local Users and Groups management console opened successfully.")

def winFeatures_access():  # Windows Features 
    exeXc("optionalfeatures", "Windows features opened successfully.")

def winGodMod_access():  # Windows GodMode Control Panel
    exeXc('explorer.exe shell:::{ED7BA470-8E54-465E-825C-99712043E01C}', "God Mode opened successfully.")

def startupFolder_access():  # Windows Startup folder
    exeXc("explorer.exe shell:startup", "Startup folder opened successfully.")

def enable_win11_Mcontext():  # Enable Windows 11 Menu Context
        command = r'reg delete "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}" /f'
        exeXc(command, "Windows 11 Menu Context enabled successfully.")

def disable_win11_Mcontext():  # Disable Windows 11 Menu Context to the old Windows 10 version
    print("Waiting for user input...")
    ret = win32api.MessageBox(0, "The Windows Explorer will be restarted...", "Warning", win32con.MB_OKCANCEL)
        
    if ret == win32con.IDOK:     
        command = r'reg add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve'
        exeXc(command, "Windows 11 Menu Context disabled successfully.")  
        subprocess.run("taskkill /f /im explorer.exe", shell=True)
        subprocess.run("start explorer.exe", shell=True)
    else:
        print("Operation cancel by user")      



