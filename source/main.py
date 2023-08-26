import json
import re
from random import randint

import requests
from bs4 import BeautifulSoup

from tgbot.config import SOURCE_DIR


def collect_data_avia():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Cookie': '__ddg1_=BIrn9ETxOE8D1mPLBad8; _rails4base_session=R0tJWXVFa1Yxb3locVF1RlY2QTltNnJ2M3pBTjNsWTN0VWk2ZHp6ME56SCs0M2wrZ3MxZW56OWJDaHBZRVdKNjN3K3gya1AzZFJhbVVueDQ3dDAyNjRhbFdFQzIvSEJ3WGZIL0FxNnhLc21VY2pnYThvczBHaFZqVC9nY1ZSNG45MGcySTZWTDc3eVhJTnNXM3ZYQ3p3PT0tLWZlMjVPeDc3aE1IaEo4SXBLczlKM1E9PQ%3D%3D--93a5c1d476b3a8e35307861149d1f88a4261160e; _ym_uid=1692987653857785185; _ym_d=1692987653; _ym_isad=2; _ym_hostIndex=0-11%2C1-0; _ym_visorc=w'
    }
    response = requests.get(url='https://izhavia.su/onlayn-servisy/onlayn-tablo/', headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')
    cards = soup.find_all('tr')
    print(f'Пожалуйста ожидайте...')

    avia_dict = {}
    for card in cards:
        card_title = card.find('td', class_='route')
        if not card_title:
            card_title = 'Нет данных'
        else:
            card_title = card_title.text.strip()
        card_time = card.find('time', class_='time')
        if not card_time:
            card_time = 'Нет данных'
        else:
            card_time = card_time.text.strip()
        card_date = card.find('time', class_='date')
        if not card_date:
            card_date = 'Нет данных'
        else:
            card_date = card_date.text.strip()

        for num in enumerate(range(randint(0, 1000000))):
            card_id = f'card_{num}'
            card_id = re.sub(r'[^a-zA-Z0-9_]', '', card_id)

        avia_dict[card_id] = {
            'card_title': f'{card_title}',
            'card_time' : f'{card_time} - {card_date}'
        }
    with open(SOURCE_DIR / 'avia.json', 'w', encoding='utf-8') as file:
        json.dump(avia_dict, file, indent=4, ensure_ascii=False)
    print(f'Загрузка расписания авиа прошла успешна...')


def collect_data_train():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Cookie': 'spravka=dD0xNjkyODIyNzk4O2k9MjEzLjIzMC4xMDIuMTAxO0Q9MzJDN0REMDE5NDYxM0VENUExQkYyQzVGMTg0RTJENUNGNzg2RTFGNkI3MzQwMjhCMEIxQkZFMEE0RTM4MjQ0NTRGQUVEQzFFQjcxMzA1N0E5RDAxRjlGOUNDQjUzQzJDNkEzNDFBNDU2M0IxRDM3MTFGOEEwNjlENTY5MDY1QUJBNTYwNENGMjI1NDg5RjE0RjY2NkJCQjg2QTM0O3U9MTY5MjgyMjc5ODc1MTkwODMxNztoPWQ1ZmY2YjA5MTRjNGNmNzI4ZTg2OWM1YzJjY2ZlY2Vm; _yasc=jEhvYJGiJjzJns3hhtPcTjL/hgRezlxxgX62eIYek1ShS4YKrMnn168tYRbUzVVE+pc=; i=BAVTSHXVTUzGC26pXibOVyKJv0k71XF0yiAx9dipx/Nn88wGHI2M/5dNnniky99VvA1T+4xuTAuXlhbaFPoGZNZbK1c=; yandexuid=3477936521692822795; experiment__everlastingStationTouchExperiment=; experiment__everlastingThreadTouchExperiment=1; experiment__experiment=; experiment__notCanonicalThreadUid=; experiment__showFlagsInConsole=; experiment__webvisor=; experiment__yabusOfflineLabel=1; fonts-loaded=true'
    }
    response = requests.get(url='https://rasp.yandex.uz/station/9612140/tablo/?event=arrival', headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')
    cards = soup.find_all('tr', class_='StationTable__tableRow')
    print(f'Пожалуйста ожидайте...')

    train_dict = {}
    for card in cards:
        card_title = card.find('a', class_='Link StationTable__threadTitle')
        if not card_title:
            card_title = 'Нет данных'
        else:
            card_title = card_title.text.strip()
        card_time = card.find('div', class_='StationTable__threadTime')
        if not card_time:
            card_time = 'Нет данных'
        else:
            card_time = card_time.text.strip()

        for num in enumerate(range(randint(0, 1000000))):
            card_id = f'card_{num}'
            card_id = re.sub(r'[^a-zA-Z0-9_]', '', card_id)

        train_dict[card_id] = {
            'card_title': f'{card_title}',
            'card_time' : f'{card_time}'
        }
    with open(SOURCE_DIR / 'train_arrival.json', 'w', encoding='utf-8') as file:
        json.dump(train_dict, file, indent=4, ensure_ascii=False)
    print(f'Загрузка расписания поездов и электричек прошла успешна...')


def collect_all_data():
    collect_data_avia()
    collect_data_train()


if __name__ == "__main__":
    collect_all_data()
