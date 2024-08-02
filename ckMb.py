import wmi

def get_motherboard_info():
    c = wmi.WMI()
    motherboard_info = []
    
    for board in c.Win32_BaseBoard():
        info = {
            "manufac_0": board.Manufacturer,
            "prod_0": board.Product,
            "serial_0": board.SerialNumber,
            "ver_0": board.Version
        }
        motherboard_info.append(info)
    
    return motherboard_info

board_finalvalue = get_motherboard_info()

# Extract individual values
if board_finalvalue:
    mb_manufact0 = board_finalvalue[0]['manufac_0']
    mb_prod0 = board_finalvalue[0]['prod_0']
    mb_serial0 = board_finalvalue[0]['serial_0']
    mb_ver0 = board_finalvalue[0]['ver_0']
else:
    mb_manufact0 = mb_prod0 = mb_serial0 = mb_ver0 = None


