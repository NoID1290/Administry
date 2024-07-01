import pyuac

if not pyuac.isUserAdmin():
    uacUservalue = " [NORMAL] "
    uac = [0]
else:
    uacUservalue = " [ADMIN MODE] "
    uac = [1]
        
