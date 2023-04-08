import subprocess
import win32api
import win32con





def WIN_GUI_KILL():
    win32api.MessageBox(0, "Windows Explorer restarting...", "Message", win32con.MB_OK)
    subprocess.run("taskkill /f /im explorer.exe", shell=True)
    subprocess.run("start explorer.exe", shell=True)




