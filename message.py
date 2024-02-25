def send_email(message, me, you):
    from _email import _send_email

    _send_email(message, me, you)


def send_discord(message):
    from _discord import send
    send(message)


def send_notification(message):
    from notification import send_notification

    # Example usage
    send_notification("vMonitor", f"{message}")


if __name__ == '__main__':
    from main import main
    main()  # .
