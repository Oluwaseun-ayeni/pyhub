import requests
from bs4 import BeautifulSoup

quotes = []


def web_scrape(page_num):
    page = str(page_num)
    URL = 'https://www.goodreads.com/quotes/tag/humor?page=' + page
    webpage = requests.get(URL)

    soup = BeautifulSoup(webpage.text, "html.parser")

    quoteText = soup.find_all('div', attrs={'class': 'quoteText'})

    for i in quoteText:
        quote = i.text.strip().split('\n')[0]
        quotes.append(quote)
        print(quote)


web_scrape(1)
