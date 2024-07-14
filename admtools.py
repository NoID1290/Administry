import os

def execute_command(command, success_message):
    try:
        os.system(command)
        print(success_message)
    except Exception as e:
        print(f"An error occurred: {e}")

def luagm_access():
    execute_command("lusrmgr.msc", "Local Users and Groups management console opened successfully.")

def winFeatures_access():
    execute_command("optionalfeatures", "Windows features opened successfully.")

def winGodMod_access():
    execute_command("explorer.exe shell:::{ED7BA470-8E54-465E-825C-99712043E01C}", "God Mode opened successfully.")

def startupFolder_access():
    execute_command("explorer.exe shell:startup", "Startup folder opened successfully.")




