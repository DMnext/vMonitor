from notify.message import send_discord, send_notification


def send_terminal(message):
    print(message)


def _error_notify(msg):
    error_msg = f"[ERROR] {msg}"
    return error_msg


def _warning_notify(msg):
    warning_msg = f"[WARNING] {msg}"
    return warning_msg


def _info_notify(msg):
    info_msg = f"[INFO] {msg}"
    return info_msg


def _notify(msg, _send_discord, _send_notification, warning_notify: bool = False, error_notify: bool = False):

    if error_notify:
        message = _error_notify(msg)

    elif warning_notify:
        message = _warning_notify(msg)

    else:
        message = _info_notify(msg=msg)

    send_terminal(message)

    if _send_discord:
        send_discord(message)

    if _send_notification:
        send_notification(message)