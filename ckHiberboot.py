import winreg

def is_fast_boot_enabled():
    try:
        # Open the key in the registry
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Power")

        # Query the value
        value, _ = winreg.QueryValueEx(reg_key, "HiberbootEnabled")
        
        # Close the key
        winreg.CloseKey(reg_key)
        
        # If the value is 1, Fast Boot is enabled; if 0, it's disabled
        return value == 1
    except FileNotFoundError:
        print("Registry key not found. Fast Boot may not be available on this system.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

status = is_fast_boot_enabled()
if status is not None:
    if status:
        hb_value0 = ("Enable")
    else:
        hb_value0 = ("Disable")
else:
    hb_value0 = ("Not available on this system.")        
