from bs4 import BeautifulSoup
import requests

user_agent = 'Chrome/52 (Macintosh; Intel Mac OS X 10_10_5); Dashiell Stander/UC Berkeley/dstander@protonmail.com'


class Ao3ScraperBase:
    base_url = 'https://www.archiveofourown.com'
    url_prefix = ''
    url_postfix = ''

    def __init__(self):
        self.user_agent = user_agent
        self.page_empty = False
        self.headers = self._make_headers

    def _make_headers(self):
        return {'user-agent': self.user_agent}

    def _make_url(self, category):
        return f'{self.url_prefix}/{category}/{self.url_postfix}'

    def get(self, url):
        return requests.get(f'{self.base_url}/{url}', headers=self.headers)

    def load(self, request):
        return BeautifulSoup(request.text, 'lxml')
    
    def scrape(self):
        raise NotImplementedError
