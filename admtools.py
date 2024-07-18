import os

def exeXc(command, success_message):
    try:
        os.system(command)
        print(success_message)
    except Exception as e:
        print(f"An error occurred: {e}")

# Windows Tools Access        

def luagm_access(): # Local User And Group Management
    exeXc("lusrmgr.msc", "Local Users and Groups management console opened successfully.")

def winFeatures_access(): # Windows Features 
    exeXc("optionalfeatures", "Windows features opened successfully.")

def winGodMod_access(): # Windows GodMode Control Panel
    exeXc("explorer.exe shell:::{ED7BA470-8E54-465E-825C-99712043E01C}", "God Mode opened successfully.")

def startupFolder_access(): # Windows Startup folder
    exeXc("explorer.exe shell:startup", "Startup folder opened successfully.")





