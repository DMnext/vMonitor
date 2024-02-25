from plyer import notification


def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="vMonitor/logo/logo.png",  # You can specify an icon file path if needed
        timeout=15  # Notification duration in seconds
    )
