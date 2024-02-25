import configparser
import yaml


def read_ini_config_value(file_path, key):
    config = configparser.ConfigParser()
    config.read(file_path)
    value = None
    for section in config.sections():
        if key in config[section]:
            value = config[section][key]
            break
    return value


def read_yaml_config_value(file_path, key):
    with open(file_path, 'r') as f:
        config_data = yaml.safe_load(f)
        value = None
        for k, v in config_data.items():
            if k == key:
                value = v
                break
    return value
