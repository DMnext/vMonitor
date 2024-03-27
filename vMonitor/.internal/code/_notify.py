from notify.message import send_discord, send_notification
from saver import save_log_line
from _os import get_log_file
import time


def send_terminal(message):
    save_log_line(message, get_log_file())
    print(message)


def _error_notify(msg):
    error_msg = f"[ERROR {time.strftime('%y.%m.%d_%H:%M:%S')}] {msg}"
    return error_msg


def _warning_notify(msg):
    warning_msg = f"[WARNING {time.strftime('%y.%m.%d_%H:%M:%S')}] {msg}"
    return warning_msg


def _info_notify(msg):
    info_msg = f"[INFO {time.strftime('%y.%m.%d_%H:%M:%S')}] {msg}"
    return info_msg


def _notify(msg, _send_discord, _send_notification, warning_notify: bool = False, error_notify: bool = False, only_log_discord: bool = False):

    if error_notify:
        message = _error_notify(msg)

    elif warning_notify:
        message = _warning_notify(msg)

    else:
        message = _info_notify(msg=msg)

    send_terminal(message)

    if _send_notification:
        send_notification(msg)

    if _send_discord:
        send_discord(message, main_channle_msg=msg, only_log=only_log_discord)
