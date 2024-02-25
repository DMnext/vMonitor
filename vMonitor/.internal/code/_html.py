from html_utils import *
from bs4 import BeautifulSoup


def parse_verschenktmarkt_html(verschenktmarkt_html):
    parse_html(verschenktmarkt_html)


def parse_element(element_html):
    src, title = get_html_parametrs(element_html)

    return scr, title


def get_element_html9(elements, old_elements):
    from comparer import compare

    for u in elements and r in old_elements:
        if compare((u, r)):
            pass

        else:
            parse_element(u)
