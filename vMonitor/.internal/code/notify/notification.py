from plyer import notification
from _os import get_logo_path

logo_path:str = get_logo_path()


def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=logo_path,  # You can specify an icon file path if needed
        timeout=10  # Notification duration in seconds
    )
