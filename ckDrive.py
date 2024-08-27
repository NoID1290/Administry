import wmi

def get_hard_drive_info():
    c = wmi.WMI()
    for disk in c.Win32_DiskDrive():
        print(f"Device ID: {disk.DeviceID}")
        print(f"Model: {disk.Model}")
        print(f"Size: {int(disk.Size) / (1024 ** 3)} GB")
        print(f"Serial Number: {disk.SerialNumber}")
        print(f"Interface Type: {disk.InterfaceType}")
        print(f"Partitions: {disk.Partitions}\n")

get_hard_drive_info()
