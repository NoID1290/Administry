import wmi

def get_ram_info():
    c = wmi.WMI()
    ram_info = []
    
    for memory in c.Win32_PhysicalMemory():
        info = {
            "bank_label_0": memory.BankLabel,
            "capacity_0": int(memory.Capacity) // (1024 ** 3),  # Convert to GB
            "speed_0": memory.Speed,
            "manufacturer_0": memory.Manufacturer,
            "part_number_0": memory.PartNumber,
            "serial_number_0": memory.SerialNumber,
            "memory_type_0": memory.MemoryType
        }
        ram_info.append(info)
    
    return ram_info

ram_finalvalue = get_ram_info()

# Extract individual values
if ram_finalvalue:
    ram_bank_label0 = ram_finalvalue[0]['bank_label_0']
    ram_capacity0 = ram_finalvalue[0]['capacity_0']
    ram_speed0 = ram_finalvalue[0]['speed_0']
    ram_manufacturer0 = ram_finalvalue[0]['manufacturer_0']
    ram_part_number0 = ram_finalvalue[0]['part_number_0']
    ram_serial_number0 = ram_finalvalue[0]['serial_number_0']
    ram_memory_type0 = ram_finalvalue[0]['memory_type_0']
else:
    ram_bank_label0 = ram_capacity0 = ram_speed0 = ram_manufacturer0 = ram_part_number0 = ram_serial_number0 = ram_memory_type0 = None
