import time as t
from timer import Timer
import os

from reader import read_yaml_config_value

from saver import prepare_to_save_log

from monitor_html.html_utils import *
from monitor_html.investigate import *
from monitor_html.html import parse_element

from error import VMError, error

import random

from _notify import _notify, send_terminal
from _os import test, get_version_contents, get_rid, load_config, get_log_file, get_cache_dir

url = "https://www.verschenkmarkt-stuttgart.de/"

timer = Timer()

messages_for_reminding = ["Join our discord: 'https://discord.gg/PTGXN7Cscy/'.",
                          f"Version: {get_version_contents()}.",
                          "Did you see the api? Go to the 'api' file.",
                          "Configure vMonitor in the 'vMonitor/.config/config.yaml' file.",
                          "MIT-license see 'LISENSE' file.",
                          "Not familiar with Verschenktmarkt? See 'https://www.verschenkmarkt-stuttgart.de/'.",
                          "New to vMonitor? Read 'README.md' for more information.",
                          "Don't forget to replace 'TOKEN' in the 'vMonitor/.config/config.yaml' file (Or you will get an error!)."
                          "Nothing interesting to show."]


def print_log(msg):
    send_terminal(f"[INFO {t.strftime('%y.%m.%d_%H:%M:%S')}] [LOG] {msg}")


def print_info(msg):
    send_terminal(f"[INFO {t.strftime('%y.%m.%d_%H:%M:%S')}] {msg}")


def print_error(msg):
    send_terminal(f"[ERROR {t.strftime('%y.%m.%d_%H:%M:%S')}] {msg}")


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
    os.makedirs(get_cache_dir(), exist_ok=True)

    rid = get_rid()
    prepare_to_save_log(get_log_file(), rid)

    print_info("Testing...")

    with timer:
        err, msg = test()
    print_log(f"Testing time: '{timer.get_real_time() * 1000:.2f}' mily seconds.")
    print_log(f"Testing time: '{timer.get_cpu_time() * 1000:.2f}' CPU time.")

    if not err:
        print_error(f"{msg}")
        raise VMError(msg)
    else:
        print_info(f"{msg}")

    print_log("Loading config...")

    with timer:

        # Example usage
        config_file_path = load_config()

        _time = read_yaml_config_value(config_file_path, 'time')
        _send_discord = read_yaml_config_value(config_file_path, 'send_discord')
        _send_notification = read_yaml_config_value(config_file_path, 'send_notification')

    # conf(err=err)

    print_log(f"Loading config time: '{timer.get_real_time() * 1000:.2f}' mily seconds.")
    print_log(f"Loading config time: '{timer.get_cpu_time() * 1000:.2f}' CPU time.")

    print_log("Calculating for startup...")

    with timer:

        time_in_secs = _time * 60

        g = 0

        time_slept = 0

        nothing_changed = 0
        somthing_changed = 0

        # URL of the webpage from which to fetch the HTML

        html = find_html(url)
        html_elements = parse_html(html)

    print_log(f"Calculating time: '{timer.get_real_time() * 1000:.2f}' mily seconds.")
    print_log(f"Calculating time: '{timer.get_cpu_time() * 1000:.2f}' CPU time.")

    message = "Started vMonitor!"

    _notify(message, _send_discord, _send_notification)

    print_info(f"Running on version {get_version_contents()}, id = {rid}!")

    while True:
        try:

            print_log("Looking for changes in Verschenktmarkt...")

            with timer:

                link, link_to_site, msg, msg2, new_changes, changed = html_monitor(old_elements=html_elements)

                html = find_html(url)
                html_elements = parse_html(html)

            print_log(f"Monitoring Verschenktmarkt time: '{timer.get_real_time() * 1000:.2f}' mily seconds.")
            print_log(f"Monitoring Verschenktmarkt time: '{timer.get_cpu_time() * 1000:.2f}' CPU time.")

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

            t_t = (10 - _time) + random.randint(1, 3)
            if t_t < 3:
                t_t = 3

            g += 1
            if g > t_t:
                g = 0
                print_log(
                    f"Number of changes = '{somthing_changed}', Number of no changes = '{nothing_changed}', time slept = {time_slept * 1000} mily seconds.")
                print_log(f"[REMINDER] {messages_for_reminding[random.randint(0, len(messages_for_reminding) - 1)]}")

        except Exception as err:

            _notify("Error in vMonitor!", _send_discord, _send_notification, error_notify=True)

            error(err)

            # print(f"--> error")

            _notify(err, _send_discord, _send_notification=False, error_notify=True)

            raise VMError("vMonitor crashed!")

        print_log("Sleeping...")

        t.sleep(time_in_secs)

        time_slept += time_in_secs


if __name__ == "__main__":
    main()
