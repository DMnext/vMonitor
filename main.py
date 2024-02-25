import time

from settings import conf
from message import send_email, send_discord, send_notification
from html_utils import write_html, find_html, parse_html
from pretty import pretty_syntax
from reader import read_yaml_config_value


def change(send_terminal, _send_discord, _send_email, _send_notification, email):
    msg = "Verschenktmarkt changed!"

    if send_terminal:
        print(msg)

    if _send_discord:
        send_discord(msg)

    if _send_email:
        send_email(msg, "vMonitor", email)

    if _send_notification:
        send_notification(msg)


def _(save_log_cache, html, send_log_terminal, send_log_email, pretty_print, email):
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
        change(send_terminal, _send_discord, _send_email, _send_notification, email)

    html = find_html(url)
    html_elements = parse_html(html)
    html_number = len(html_elements)
    return html, html_elements, html_number


def main():
    # Example usage
    config_file_path = 'config.yaml'

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

    conf(err=err)

    time_in_secs = _time * 60

    if pretty_print and send_terminal:
        from terminal import install_traceback
        # install_traceback()

    # if send_terminal and pretty_print:
    #     from terminal import console
    #     console()
    #     _console = pretty_spinner()

    # URL of the webpage from which to fetch the HTML
    url = "https://www.verschenkmarkt-stuttgart.de/"

    html_elements = []
    html_number = 0

    html, html_elements, html_number = communicate_with_internet(url=url,
                                                                 html_elements=html_elements,
                                                                 html_number=html_number,
                                                                 send_terminal=send_terminal,
                                                                 _send_discord=_send_discord,
                                                                 _send_email=_send_email,
                                                                 _send_notification=_send_notification,
                                                                 email=email, )

    message = "Started vMonitor!"

    if send_terminal:
        print(message)

    if _send_notification:
        send_notification(message)

    if _send_discord:
        send_discord(message)

    send_email("hello!", "vMonitor", email)

    while True:
        try:
            html, html_elements, html_number = communicate_with_internet(url=url,
                                                                         html_elements=html_elements,
                                                                         html_number=html_number,
                                                                         send_terminal=send_terminal,
                                                                         _send_discord=_send_discord,
                                                                         _send_email=_send_email,
                                                                         _send_notification=_send_notification,
                                                                         email=email, )

            _(save_log_cache=save_log_cache,
              html=html,
              send_log_terminal=send_log_terminal,
              send_log_email=send_log_email,
              pretty_print=pretty_print,
              email=email)

        except:

            msg = "Error in vMonitor"

            if _send_discord:
                send_discord(msg)
            if _send_notification:
                send_notification(msg)
            if send_terminal:
                print(msg)
            if send_log_email:
                send_email(msg, "vMonitor", email)

        time.sleep(time_in_secs)


if __name__ == "__main__":
    main()

