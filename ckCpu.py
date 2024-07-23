import cpuinfo
import platform
import psutil

def get_cpu_info():
    # Get CPU information using py-cpuinfo
    cpu_info = cpuinfo.get_cpu_info()
    
    # Get basic CPU details using psutil
    cpu_info_data = {
        'CPU Name': cpu_info['brand_raw'],
        'Arch': platform.architecture()[0],
        'Physical Cores': psutil.cpu_count(logical=False),
        'Logical Cores': psutil.cpu_count(logical=True),
        'CPU Frequency (MHz)': psutil.cpu_freq().max,
        'CPU Core Count': psutil.cpu_count(),
        'CPU Usage (%)': psutil.cpu_percent(interval=1),
        'CPU L2 Cache Size (KB)': cpu_info.get('l2_cache_size', 'N/A'),
        'CPU L3 Cache Size (KB)': cpu_info.get('l3_cache_size', 'N/A')
    }
    
    return cpu_info_data

cpu_info_data = get_cpu_info()

# Extract individual values
CPU_Name = cpu_info_data['CPU Name']
Arch = cpu_info_data['Arch']
Physical_Cores = cpu_info_data['Physical Cores']
Logical_Cores = cpu_info_data['Logical Cores']
CPU_Frequency = cpu_info_data['CPU Frequency (MHz)']
CPU_Core_Count = cpu_info_data['CPU Core Count']
CPU_Usage = cpu_info_data['CPU Usage (%)']
L2_Cache_Size = cpu_info_data['CPU L2 Cache Size (KB)']
L3_Cache_Size = cpu_info_data['CPU L3 Cache Size (KB)']


'''
# Print the CPU information
if cpu_info_data:
    for key, value in cpu_info_data.items():
        print(f"{key}: {value}")
else:
    CPU_Name = Arch = Physical_Cores = Logical_Cores = CPU_Frequency = CPU_Core_Count = CPU_Usage = L2_Cache_Size = L3_Cache_Size = None
'''