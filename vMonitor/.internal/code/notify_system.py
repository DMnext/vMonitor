from _notify import _notify
from _os import load_config
from reader import read_yaml_config_value


def _communicate(msg, error: bool = False, warning: bool = False):
    # Example usage
    config_file_path = load_config()

    _time = read_yaml_config_value(config_file_path, 'time')
    _send_discord = read_yaml_config_value(config_file_path, 'send_discord')
    _send_email = read_yaml_config_value(config_file_path, 'send_email')
    _send_notification = read_yaml_config_value(config_file_path, 'send_notification')

    _notify(msg=msg,
            _send_discord=_send_discord,
            _send_notification=_send_notification,
            error_notify=error,
            warning_notify=warning)
