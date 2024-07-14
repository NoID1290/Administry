import os


#Accessing Windows Tools

def luagm_access(): # Local Users and Groups management
    try:
        os.system("lusrmgr.msc")
        print("Local Users and Groups management console opened successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def winFeatures_access(): # Windows Features 
    try:
        os.system("optionalfeatures")     
        print("Windows features open")   
    except Exception as e:
        print(f"An error occurred: {e}")

def winGodMod_access(): # Windows God Mode Control Panel
    try:
        os.system("explorer.exe shell:::{ED7BA470-8E54-465E-825C-99712043E01C}")          
        print("Open God Mode")
    except Exception as e:
        print(f"An error occurred: {e}") 






