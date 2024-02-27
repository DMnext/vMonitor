from _notify import _notify
from _os import load_config
from reader import read_yaml_config_value
from notify.pretty import errorhandle


def _communicate(msg):
    # Example usage
    config_file_path = load_config()

    _time = read_yaml_config_value(config_file_path, 'time')
    send_terminal = read_yaml_config_value(config_file_path, 'send_terminal')
    _send_discord = read_yaml_config_value(config_file_path, 'send_discord')
    _send_email = read_yaml_config_value(config_file_path, 'send_email')
    _send_notification = read_yaml_config_value(config_file_path, 'send_notification')
    email = read_yaml_config_value(config_file_path, 'save_log_cache')

    _notify(msg=msg, send_terminal=send_terminal,
            _send_discord=_send_discord,
            _send_email=_send_email,
            _send_notification=_send_notification,
            email=email)


def handle_err(errormessage: str | None = None):
    _communicate(f"Error: {errormessage}")
    errorhandle(err="PRETTY POOP!", errormessage=errormessage)
