import requests
from bs4 import BeautifulSoup
import json

items = {}


def dvsota(url: str):
    """
    Function to extract product names and prices from the DvSota website.

    Args:
        url (str): URL of the product page.

    Returns:
        str: Error message or empty string if no errors occurred.
    """
    response = requests.get(url)

    if response.status_code == 200:
        src = response.text
        soup = BeautifulSoup(src, 'lxml')
        product_name = soup.find('h1', class_="product_name title").text.strip()
        price_head = soup.find('div', class_="product_price__head").find('p', class_="product_price__sum").text.strip().rstrip(' ₽').replace(' ', '')
        items[product_name] = price_head
        with open('items.json', 'w', encoding='utf-8') as file:
            json.dump(items, file, ensure_ascii=False, indent=2)
        return ""
    else:
        return f'Error: {response.status_code}'


print(dvsota('https://dvsota.ru/catalog/smartfony/iphone/iphone-14/13922-smartfon-apple-iphone-14-128gb-midnight'))