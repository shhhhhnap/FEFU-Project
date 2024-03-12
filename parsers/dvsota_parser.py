import requests
from bs4 import BeautifulSoup


def dvsota(url: str):
    headers = {
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'accept': '*/*'
    }
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, 'lxml')
        product_name = soup.find('h1', class_='product_name title').text.strip().rstrip('\n')
        product_price = (soup.find('p', class_='product_price__sum').text.strip().rstrip(' ₽').
                         replace(' ', ''))
        return product_name, product_price
    return req.status_code


