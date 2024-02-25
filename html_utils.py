import os
import random
import time
import requests
from bs4 import BeautifulSoup


def write_html(html) -> str:
    html_random = random.randint(0, 1000)
    html_time = time.strftime("%y.%m.%d_%H:%M:%S")
    path = f"VMonitor/.cache/html/html-{html_time}-{html_random}"
    path2 = "VMonitor/.cache/html/html/"
    fh = None
    while True:
        try:
            fh = open(path)
            break
        except FileNotFoundError:
            os.makedirs(path2)
            continue
    assert fh is not None
    fh.write(html)
    return path


def find_html(url):

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, "html.parser")

        # Get the entire HTML code
        html_code = soup.prettify()

        # Print or manipulate the HTML code as needed
        return html_code
    else:
        errmsg = f"Failed to retrieve HTML code. Status code: {response.status_code}"
        raise ConnectionError(errmsg)
    # https://www.verschenkmarkt-stuttgart.de/


def parse_html(html_code):

    list_of_items = []

    # Example HTML code
    # html_code = """
    # <html>
    # <head>
    # <title>Example HTML</title>
    # </head>
    # <body>
    # <h1>Welcome to BeautifulSoup</h1>
    # <p>This is a paragraph.</p>
    # <ul>
    #   <li>Item 1</li>
    #   <li>Item 2</li>
    #   <li>Item 3</li>
    # </ul>
    # </body>
    # </html>
    # """
    #
    # Parse the HTML code
    soup = BeautifulSoup(html_code, 'html.parser')

    # Extract specific elements
    # title = soup.title
    # listing_card_list = soup.find("#listing-card-list")
    # paragraph = soup.find('p')
    listing_card_list_items = soup.find_all("#card listing-card   ")

    # Print the text content of the elements
    # print("Title:", title.text)
    # print("H1:", h1.text)
    # print("Paragraph:", paragraph.text)
    # print("List Items:")
    for item in listing_card_list_items:
        list_of_items.append(item.text)
    return list_of_items


if __name__ == '__main__':
    from main import main
    main()
