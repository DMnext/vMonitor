import time

# from settings import conf
from reader import read_yaml_config_value

from stop_all_proseses import *

from comparer import compare

from _notify import _notify
from _monitor_html import *
from _os import load_config

url = "https://www.verschenkmarkt-stuttgart.de/"


def html_monitor(old_elements):

    new_changes = 0

    changed = False

    msg = None
    link = None

    elements = parse_html(find_html(url=url))

    for u, r in zip(elements, old_elements):
        if compare((u, r)):
            pass

        else:
            if not investigate(element=u, old_element=r):
                new_changes += 1
                link, msg = parse_element(u)
                changed = True

    if msg is not None and link is not None:

        return link, msg, new_changes, changed


def fast_notify(save_log_cache, send_log_terminal, send_log_email, pretty_print, email, html):
    _b(save_log_cache=save_log_cache,
       html=html,
       send_log_terminal=send_log_terminal,
       send_log_email=send_log_email,
       pretty_print=pretty_print,
       email=email)


def main():
    global url
    # Example usage
    config_file_path = load_config()

    _time = read_yaml_config_value(config_file_path, 'time')
    send_terminal = read_yaml_config_value(config_file_path, 'send_terminal')
    _send_discord = read_yaml_config_value(config_file_path, 'send_discord')
    _send_email = read_yaml_config_value(config_file_path, 'send_email')
    _send_notification = read_yaml_config_value(config_file_path, 'send_notification')
    pretty_print = read_yaml_config_value(config_file_path, 'pretty')
    email = read_yaml_config_value(config_file_path, 'save_log_cache')
    send_log_terminal = read_yaml_config_value(config_file_path, 'send_log_terminal')
    send_log_email = read_yaml_config_value(config_file_path, 'send_log_terminal')
    err = read_yaml_config_value(config_file_path, 'email')
    save_log_cache = read_yaml_config_value(config_file_path, 'save_log_cache')

    # conf(err=err)

    time_in_secs = _time * 60

    if pretty_print and send_terminal:
        pass
        # install_traceback()

    # if send_terminal and pretty_print:
    #     from terminal import console
    #     console()
    #     _console = pretty_spinner()

    # URL of the webpage from which to fetch the HTML

    html = find_html(url)
    html_elements = parse_html(html)
    html_number = len(html_elements)


    html_elements = []
    html_number = 0

    html, html_elements, html_number = communicate_with_internet(url=url,
                                                                 html_elements=html_elements,
                                                                 html_number=html_number,
                                                                 )

    message = "Started vMonitor!"

    _notify(message, send_terminal, _send_discord, _send_email, _send_notification, email)

    while True:
        try:
            html, html_elements, html_number = communicate_with_internet(url=url,
                                                                         html_elements=html_elements,
                                                                         html_number=html_number)

            if get_communication_with_internet_result():
                _notify("", send_terminal, _send_discord, _send_email, _send_notification, email)

            fast_notify(save_log_cache, send_log_terminal, send_log_email, pretty_print, email, html)

        except Exception:

            stop("Error in vMonitor", 1)

        time.sleep(time_in_secs)


if __name__ == "__main__":
    main()
