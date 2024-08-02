import platform

def get_Win_Build():
    # Get the OS version info from platform module
    os_version = platform.version()
    system = platform.system()
    release = platform.release()


    # Collecting values
    os_info = {
        'ver': os_version,
        'sys': system,
        'build': release,
    }

    return os_info

osBuildVersion = get_Win_Build()

# Extract individual value
os_VER0 = osBuildVersion['ver']
sys_0 = osBuildVersion['sys']
build_0 = osBuildVersion['build']

#Format

ckOS__finalV = f"{sys_0} {build_0} (Version {os_VER0})"


