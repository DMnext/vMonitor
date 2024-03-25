from monitor_html.html_utils import *
from monitor_html.investigate import *
from monitor_html.html import parse_element
from main import html_monitor


def get_html():
    return find_html(url="https://www.verschenkmarkt-stuttgart.de/"))


def parse_verschenktmarkt_html(HTML):
    return parse_html(HTML)

    
def invesgate_html(element, old_element):
    return investigate(element, old_element)


def check_for_html(old_elements):
    return html_monitor(old_elements)
