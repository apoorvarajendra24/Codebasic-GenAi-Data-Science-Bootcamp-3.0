import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup
import re

def print_unicode_grid(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()

    grid = {}

    for line in text.splitlines():
        match = re.findall(r'(\S)\s+(\d+)\s+(\d+)', line)
        if match:
            char, x, y = match[0]
            grid[(int(x), int(y))] = char

    if not grid:
        print("No valid data found")
        return

    max_x = max(x for x, _ in grid)
    max_y = max(y for _, y in grid)

    for y in range(max_y, -1, -1):
        row = ""
        for x in range(max_x + 1):
            row += grid.get((x, y), " ")
        print(row)

url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
url1= "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
print_unicode_grid(url)