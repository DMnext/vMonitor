from monitor_html.html_utils import find_html, parse_html
from monitor_html._html import parse_element
from monitor_html.investigate import investigate

communication_with_internet_result = None


def communicate_with_internet(url,
                              html_elements,
                              html_number):

    global communication_with_internet_result

    if parse_html(
            find_html(url)) != html_elements and html_elements is not None and html_number != 0 and html_number != len(
                parse_html(find_html(url))):
        communication_with_internet_result = True
    else:
        communication_with_internet_result = False
        # change(send_terminal, _send_discord, _send_email, _send_notification, email)

    html = find_html(url)
    html_elements = parse_html(html)
    html_number = len(html_elements)
    return html, html_elements, html_number


def get_communication_with_internet_result():
    global communication_with_internet_result
    return communication_with_internet_result


def get_element_html9(elements, old_elements):
    from comparer import compare

    for u, r in zip(elements, old_elements):
        if compare((u, r)):
            pass

        else:
            if not investigate(element=u, old_element=r):
                parse_element(u)


def get_get_element_html9_result():
    global communication_with_internet_result
    return communication_with_internet_result
