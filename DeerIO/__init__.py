import bs4
import re
import requests
import time
import calendar


class CustomError(Exception):
    pass


def get_bs4(html: str) -> bs4.BeautifulSoup:
    return bs4.BeautifulSoup(html, 'html.parser')


def get_shops(soup: bs4.BeautifulSoup) -> list:
    return soup.find_all('div', class_='shop-result')


def get_shop_create_time(since: str) -> float:
    create_time = re.search('[\d\.]+', since).group()

    return calendar.timegm(time.strptime(create_time, '%d.%m.%Y'))


def get_json(shops: list) -> dict:
    shops_result = []
    items = []

    for shop in shops:
        shop_info = shop.find('div', class_='info-block')
        shop_header = shop_info.find('a', class_='shop-title')

        shops_result.append({
            'id': len(shops_result),
            'title': shop_header.get_text(),
            'link': shop_header['href'],
            'since': get_shop_create_time(shop_info.find('span', class_='since').get_text()),
            'description': shop_info.find('div', class_='help-block').get_text().strip()
        })

        table_rows = shop.find_all('tr', itemtype="http://schema.org/Product")

        for row in table_rows:
            column = row.find_all('td')

            items.append({
                'shop_id': len(shops_result) - 1,  # Because we just add a shop in our list up there
                'title': column[0].find('div', class_='good-title').get_text().strip(),
                'count': int(column[1].get_text()),
                'price': float(column[2].find('span', class_='wowlight').get_text())
            })

    return {
        'shops': shops_result,
        'items': items
    }


def search(search_string: str, out_of_stock: bool = False) -> dict:
    try:
        if not search_string:
            raise CustomError('No query provided')

        base_url = 'https://rents.ws/ru/search/'
        params = {
            'q': search_string,
            'outofstock': 'on' if out_of_stock else None
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            html = response.text

            if html:
                soup = get_bs4(html)

                shops = get_shops(soup)
                return get_json(shops)

            raise CustomError('Can\'t get html from deer.io')

        else:
            raise CustomError('Error getting data from deer.io')

    except CustomError as e:
        return {'status': 'error', 'description': '{error}'.format(error=e)}
