import platform
import os
import getpass
import socket

def get_system_info():
    # Get username
    username = getpass.getuser()

    # Get operating system information
    os_info = platform.uname()
    system = os_info.system
    node_name = os_info.node
    release = os_info.release
    version = os_info.version
    machine = os_info.machine
    processor = os_info.processor

    # Get host name
    host_name = socket.gethostname()

    # Get IP address
    ip_address = socket.gethostbyname(host_name)

    # Print system information
    info = f"""User: '{username}'
Operating System: '{system}'
Node Name: '{node_name}'
Release: '{release}'
Version: '{version}'
Machine: '{machine}'
Processor: '{processor}'
Host Name: '{host_name}'
IP Address: '{ip_address}'
"""
    
    
    """
    print("User:", username)
    print("Operating System:", system)
    print("Node Name:", node_name)
    print("Release:", release)
    print("Version:", version)
    print("Machine:", machine)
    print("Processor:", processor)
    print("Host Name:", host_name)
    print("IP Address:", ip_address)
    """
    
    return info

if __name__ == "__main__":
    print(get_system_info())
