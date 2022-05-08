import bs4
import requests
from head import HEADERS
import re


def web_scrapping_habr():
    url = 'https://habr.com/ru/all'
    KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'краткое']

    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    text = response.text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('article')
    for article in articles:
        hubs = article.find_all(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
        hubs = set(hub.text.strip() for hub in hubs)
        for hub in hubs:
            text = re.findall('[a-zа-яё]+', hub, flags=re.IGNORECASE)
            for t in text:
                if t in KEYWORDS:
                    href = article.find(class_='tm-article-snippet__title-link').attrs['href']
                    link = url.replace('/ru/all', '') + href
                    title = article.find('h2').find('span').text
                    date = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title']
                    result = f"{date} - {title} - {link}"
                    print(result)


if __name__ == '__main__':
    web_scrapping_habr()

