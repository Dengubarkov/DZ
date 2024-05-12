import csv

import requests
from bs4 import BeautifulSoup
import re


def main():
    url = 'https://74.ru/text/science/'
    get_data(get_html(url))


def get_html(url):
    return requests.get(url).text

def hosturl(path):
    return f"https://74.ru{path}"

def correct_view(text):
    return re.sub(r"\D","",text)
def csv_write(data):
    with open("news.csv", 'a') as f:
        row = csv.writer(f,lineterminator="\r", delimiter=";")
        if row.writerow((data['title'], data['view'], data['url'])):
            print(f"Новость '{data['title'][0:10]}...' -----Сохранена")

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    news = soup.find_all("article", class_='_7ZOEp')
    for card in news:
        title = card.find('h3').text
        url = hosturl(card.find('a', class_='X+rcf')['href'])
        view = correct_view(card.find('span', class_='_3mETe').text)
        data = {'title': title,
                'url': url,
                'view': view}
        csv_write(data)




if __name__ == '__main__':
    main()
