import wmi

def get_ram_info():
    c = wmi.WMI()
    ram_info = []
    
    for idx, memory in enumerate(c.Win32_PhysicalMemory()):
        info = {
            f"bank_label_{idx}": memory.BankLabel,
            f"capacity_{idx}": int(memory.Capacity) // (1024 ** 3),  # Convert to GB
            f"speed_{idx}": memory.Speed,
            f"manufacturer_{idx}": memory.Manufacturer,
            f"part_number_{idx}": memory.PartNumber,
            f"serial_number_{idx}": memory.SerialNumber,
            f"memory_type_{idx}": memory.MemoryType
        }
        ram_info.append(info)
    
    return ram_info

ram_finalvalue = get_ram_info()

# Extract individual values for all modules
if ram_finalvalue:
    for idx, ram in enumerate(ram_finalvalue):
        globals()[f'ram_bank_label{idx}'] = ram[f'bank_label_{idx}']
        globals()[f'ram_capacity{idx}'] = ram[f'capacity_{idx}']
        globals()[f'ram_speed{idx}'] = ram[f'speed_{idx}']
        globals()[f'ram_manufacturer{idx}'] = ram[f'manufacturer_{idx}']
        globals()[f'ram_part_number{idx}'] = ram[f'part_number_{idx}']
        globals()[f'ram_serial_number{idx}'] = ram[f'serial_number_{idx}']
        globals()[f'ram_memory_type{idx}'] = ram[f'memory_type_{idx}']
else:
    # Handle the case where no RAM information is found
    ram_bank_label0 = ram_capacity0 = ram_speed0 = ram_manufacturer0 = ram_part_number0 = ram_serial_number0 = ram_memory_type0 = None
