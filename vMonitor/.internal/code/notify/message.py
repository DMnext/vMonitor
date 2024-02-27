def send_discord(message):
    from notify._discord import send
    send(message)


def send_notification(message):
    from notification import send_notification

    # Example usage
    send_notification("vMonitor", f"{message}")

# .
