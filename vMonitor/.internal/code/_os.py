import os

code_file = os.path.basename(__file__)
internal_file = os.path.basename(code_file)
vmonitor_file = os.path.basename(internal_file)
_file = os.path.basename(vmonitor_file)

config_path = f"{vmonitor_file}/.config/config.yaml"
config_dir = f"{vmonitor_file}/.config/"
cache_dir = f"{vmonitor_file}/.cache/"
license_path = f"{_file}/LISENSE"
license_dir = f"{_file}"
