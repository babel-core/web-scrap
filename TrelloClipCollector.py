from selenium import webdriver
from bs4 import BeautifulSoup

class TrelloClipCollector:

    def __init__(self):
        self.clips = {}        

    def collect(self, url):
        browser = webdriver.PhantomJS()
        browser.implicitly_wait(3)        
        browser.get(url)

        page = browser.page_source
        browser.close()

        parser = BeautifulSoup(page, 'html.parser')
        contents = parser.select('div.list')
        self.clips.clear()
        for content in contents:
            title = str(content.select_one('h2').text)
            details =  content.select('div.list-card-details > span.list-card-title')
            items = []
            for detail in details:
                id_ = str(detail.select_one('.card-short-id').text)
                item = str(detail.get_text()).replace(id_, '')
                items.append(item)
            if title != '업계동향':
                items.append(title)        
            self.clips[title] = items
        return self.clips
