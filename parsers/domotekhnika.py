import requests
from bs4 import BeautifulSoup


def domotekhnika_parser(url):
    headers = {
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'accept': '*/*'
    }

    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, 'lxml')
        product_name = soup.find('h1', class_='font-bold text-xl md:text-3xl max-w-[80%]').text.strip().rstrip('\n')
        product_price = (soup.find('div', class_='font-bold text-[2rem]')).text
        product_price= product_price.replace(u'\xa0', u'').replace('  ₽', '')
        return product_name, product_price


