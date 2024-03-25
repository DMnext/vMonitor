import time as t

from reader import read_yaml_config_value

from monitor_html.html_utils import *
from monitor_html.investigate import *
from monitor_html.html import parse_element

from error import VMError, error

from _notify import _notify
from _os import load_config

from _os import test, get_version_contents

url = "https://www.verschenkmarkt-stuttgart.de/"


def print_log(msg):
    print(f"[INFO {t.strftime('%y.%m.%d_%H:%M:%S')}] [LOG] {msg}")


def html_monitor(old_elements):

    new_changes = 0

    changed = False

    msg = None
    link = None

    link_to_site = None
    msg2 = None

    elements = parse_html(find_html(url=url))

    for u, r in zip(elements, old_elements):
        if u == r:
            pass

        else:
            if investigate(element=u, old_element=r):
                new_changes += 1
                link_to_site, msg2 = extract_link(u)
                link, msg = parse_element(u)
                changed = True

    return link, link_to_site, msg, msg2, new_changes, changed


def main():

    print(f"[INFO {t.strftime('%y.%m.%d_%H:%M:%S')}] Testing...", end="\n")

    err, msg = test()
    if not err:
        print(f"[ERROR {t.strftime('%y.%m.%d_%H:%M:%S')}] {msg}")
        raise VMError(msg)

    print(f"[INFO {t.strftime('%y.%m.%d_%H:%M:%S')}] {msg}")

    print_log("Loading config...")

    # Example usage
    config_file_path = load_config()

    _time = read_yaml_config_value(config_file_path, 'time')
    _send_discord = read_yaml_config_value(config_file_path, 'send_discord')
    _send_email = read_yaml_config_value(config_file_path, 'send_email')
    _send_notification = read_yaml_config_value(config_file_path, 'send_notification')

    # conf(err=err)

    print_log("Calculating for startup...")

    time_in_secs = _time * 60

    g = 0
    
    time_slept = 0

    nothing_changed = 0
    somthing_changed = 0

    # URL of the webpage from which to fetch the HTML

    html = find_html(url)
    html_elements = parse_html(html)

    message = "Started vMonitor!"

    _notify(message, _send_discord, _send_notification)
    
    print(f"[INFO {t.strftime('%y.%m.%d_%H:%M:%S')}] Running on version {get_version_contents()}!")

    while True:
        try:

            print_log("Looking for changes in Verschenktmarkt...")

            link, link_to_site, msg, msg2, new_changes, changed = html_monitor(old_elements=html_elements)

            html = find_html(url)
            html_elements = parse_html(html)

            if changed:
                change_text = f"""Verschenktmarkt has changed {new_changes} time(s)!
Changes:
    product_text1: "{msg}"
    product_text2: "{msg2}"
    product_photo_link: "{link}"
    product_link: "{link_to_site}"
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

            g += 1

            if g > 9:
                g = 0
                print_log(f"Number of changes = '{somthing_changed}', Number of no changes = '{nothing_changed}', time slept = {time_slept * 1000} mily secs.")

        except Exception as err:

            _notify("Error in vMonitor!", _send_discord, _send_notification,  error_notify=True)
            
            error(err)
            
            # print(f"--> error")
            
            _notify(err, _send_discord, _send_notification=False,  error_notify=True)

            raise VMError("vMonitor crashed!")

        t.sleep(time_in_secs)
        
        time_slept += time_in_secs


if __name__ == "__main__":
    main()
