import os
import time
import random
from system import get_system_info

code_file = os.path.dirname(__file__)
internal_file = os.path.dirname(code_file)
vmonitor_file = os.path.dirname(internal_file)
_file = os.path.dirname(vmonitor_file)

config_path = f"{vmonitor_file}/.config/config.yaml"
config_dir = f"{vmonitor_file}/.config/"
cache_dir = f"{vmonitor_file}/.cache/"
version_path = f"{vmonitor_file}/version"
logo_path = f"{internal_file}/logo/logo.png"
logo_dir = os.path.dirname(logo_path)
license_path = f"{_file}/LICENSE"
license_dir = f"{_file}"

code_file_name = os.path.basename(code_file)
internal_file_name = os.path.basename(internal_file)
vmonitor_file_name = os.path.basename(vmonitor_file)
version_name = os.path.basename(version_path)

license_file_name = os.path.basename(license_path)
config_dir_name = os.path.basename(config_dir)
config_file_name = os.path.basename(config_path)
logo_dir_name = os.path.basename(logo_dir)
logo_name = os.path.basename(logo_path)

rid = random.random()


def scan_dir(path):
    dir = [os.path.basename(dir.path) for dir in os.scandir(path)]
    return dir


vmonitor_file_contents = scan_dir(vmonitor_file)
license_dir_contents = scan_dir(license_dir)
config_dir_contents = scan_dir(config_dir)

license_contents = """MIT License

Copyright (c) 2024 Daniel Mayorov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

config_contents = """time: 5  # Time.
email: "example@email.com"  # Your email.

send_discord: true  # Send to Discord or Notification.
send_notification: true  # Send to Discord or Notification.

discord_token: "TOKEN"  # Discord token.
err: false  # Error.

"""


def test() -> tuple[bool, str]:

    if not ".config" in vmonitor_file_contents:
        # print(vmonitor_file_contents)
        os.mkdir(f"{vmonitor_file}/.config")
        fh = open(f"{vmonitor_file}/.config/config.yaml", "w+")
        fh.write(config_contents)
    
    if not "version" in vmonitor_file_contents:
        return False, "No 'version' file found."

    if not "LICENSE" in license_dir_contents:
        # print(license_dir_contents)
        return False, "No 'LICENSE' file found."

    # Open the file in read mode
    with open(license_path, 'r') as file:
        # Read the entire contents of the file
        file_contents = file.read()
        # print(file_contents)

    if file_contents != license_contents:
        return False, "Wrong license contents."

    elif vmonitor_file_name != "vMonitor":
        # print(vmonitor_file_name)
        return False, f"No 'vMonitor' file in '{_file}'."

    elif internal_file_name != ".internal":
        return False, f"No '.internal' file in '{vmonitor_file}'."

    elif code_file_name != "code":
        return False, f"No 'code' file in '{internal_file}'."

    elif logo_dir_name != "logo":
        print(logo_dir_name)
        return False, f"No 'logo' file in '{internal_file}'."

    elif logo_name != "logo.png":
        return False, f"No 'logo.png' file in '{internal_file}/logo/'."
        
    elif version_name != "version":
        return False, f"No 'version' file in '{internal_file}'."
        
    with open(version_path, 'r') as file:
       # Read the entire contents of the file
       file_contents = file.read()
       # print(file_contents)
   
    if file_contents != "1.0.3":
        return False, "Wrong version contents."
        
    get_system_info()
    
    return True, "Test successive!"


def load_config():
    return config_path


def get_logo_path():
    return logo_path
    
    
def get_version_contents():
    with open(version_path, 'r') as file:
       # Read the entire contents of the file
       file_contents = file.read()
       # print(file_contents)
    return file_contents
    
    
def get_log_file():
    return f"{cache_dir}LOG_{time.strftime('%y.%m.%d')}-{rid}.txt"
    
    
def get_rid():
    return rid
    

def get_cache_dir():
    return cache_dir
