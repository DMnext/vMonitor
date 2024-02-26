import os

code_file = os.path.dirname(__file__)
internal_file = os.path.dirname(code_file)
vmonitor_file = os.path.dirname(internal_file)
_file = os.path.dirname(vmonitor_file)

config_path = f"{vmonitor_file}/.config/config.yaml"
config_dir = f"{vmonitor_file}/.config/"
cache_dir = f"{vmonitor_file}/.cache/"
license_path = f"{_file}/LISENSE"
license_dir = f"{_file}"


def check():
    pass


def load_config():
    global config_path
    return config_path
