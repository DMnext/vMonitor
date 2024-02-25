import time

from settings import conf
from message import send_email, send_discord, send_notification
from html_utils import write_html, find_html, parse_html
from pretty import pretty_syntax
from reader import read_yaml_config_value


def communicate_with_internet(url,
                              html_elements,
                              html_number,
                              send_terminal,
                              _send_discord,
                              _send_email,
                              _send_notification,
                              email):
    if parse_html(
            find_html(url)) != html_elements and html_elements is not None and html_number != 0 and html_number != len(
                parse_html(find_html(url))):
        pass
        # change(send_terminal, _send_discord, _send_email, _send_notification, email)

    html = find_html(url)
    html_elements = parse_html(html)
    html_number = len(html_elements)
    return html, html_elements, html_number
