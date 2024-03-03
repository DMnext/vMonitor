import time

from reader import read_yaml_config_value

from stop_all_proseses import *

from comparer import compare

from error import error

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
    
    else:
        
        return None, None, 0, False


def main():
    global url
    
    # Example usage
    config_file_path = load_config()

    _time = read_yaml_config_value(config_file_path, 'time')
    send_terminal = read_yaml_config_value(config_file_path, 'send_terminal')
    _send_discord = read_yaml_config_value(config_file_path, 'send_discord')
    _send_email = read_yaml_config_value(config_file_path, 'send_email')
    _send_notification = read_yaml_config_value(config_file_path, 'send_notification')

    # conf(err=err)

    time_in_secs = _time * 60

    nothing_changed = 0
    somthing_changed = 0

    # URL of the webpage from which to fetch the HTML

    html = find_html(url)
    html_elements = parse_html(html)

    message = "Started vMonitor!"

    _notify(message, _send_discord, _send_notification)


    while True:
        try:

            link, msg, new_changes, changed = html_monitor(old_elements=html_elements)

            html = find_html(url)
            html_elements = parse_html(html)

            if changed:
                change_text = f"""Verschenktmarkt has changed {new_changes} times!
Changes:
    product_text: "{msg}"
    product_photo_link: "{link}"
    product_link: "error"
"""
                _notify(change_text,
                        _send_discord,
                        _send_notification)
                
                somthing_changed += 1

            else:
                _notify("Nothing changed on Verschenktmarkt...",
                        _send_discord,
                        _send_notification=False,
                        only_log_discord=True)
                
                nothing_changed += 1

        except Exception as err:

            _notify("Error in vMonitor!", _send_discord, _send_notification,  error_notify=True)
            
            error(err)
            
            # print(f"--> error")
            
            _notify(err, _send_discord, _send_notification=False,  error_notify=True)
            
            stop(1)

        time.sleep(time_in_secs)


if __name__ == "__main__":
    main()
