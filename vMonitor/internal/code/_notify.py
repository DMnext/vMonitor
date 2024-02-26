from notify.message import send_email, send_discord, send_notification
from monitor_html.html_utils import write_html
from notify.pretty import pretty_syntax


def _notify(msg, send_terminal, _send_discord, _send_email, _send_notification, email):
    if send_terminal:
        print(msg)

    if _send_discord:
        send_discord(msg)

    if _send_email:
        send_email(msg, "vMonitor", email)

    if _send_notification:
        send_notification(msg)


def _b(save_log_cache, html, send_log_terminal, send_log_email, pretty_print, email):
    if save_log_cache:
        path = write_html(html)

        if send_log_terminal:
            print(f"Success in saving cache, you can view it in '{path}'.")

    if send_log_email:
        send_email(html, "VMonitor", email)

    if send_log_terminal:
        if pretty_print:
            pretty_syntax(html, "html")
        else:
            print(html)