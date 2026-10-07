import requests
from bs4 import BeautifulSoup
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Referer': 'https://google.com'
}

session = requests.session()
site = 'https://www.miit.ru'
session.post(site, headers=headers)


def study_group_numbers():
    with open("post_WEB.json", "r", encoding="utf-8") as f:
        post = json.load(f)

    response = session.get(site + '/timetable', headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = []

    for i in soup.find('div', class_='info-block info-block_collapse show', id=post["institute"]).find_all('a', class_='dropdown-item'):
        data.append((i.text.replace('\r\n', '').replace(' ', ''), i.get("href").split('/')[-1]))

    return data

def get_all_audiences():
    for i in study_group_numbers():
        response = session.get(site+"/timetable/"+i[1], headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        for j in soup.find_all('a', class_='timetable-icon-link icon-location'):
            print(j.text)
        break



if __name__ == "__main__":
    get_all_audiences()