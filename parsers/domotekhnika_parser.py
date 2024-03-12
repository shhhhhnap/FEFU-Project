import requests
from bs4 import BeautifulSoup


def domotekhnika(url):
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
        mod_product_price = []
        for elem in product_price:
            if elem != ' ' and elem != '\xa0' and elem.isdigit():
                mod_product_price.append(elem)
        mod_product_price = ''.join(mod_product_price)
        return product_name, mod_product_price
    return req.status_code


