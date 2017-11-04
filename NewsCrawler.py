from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import parse

class NewsCrawler:

    def __init__(self):        
        self.urls = []

    def get(self, naverSearchUrl, searhItems):
        browser = webdriver.PhantomJS()
        browser.implicitly_wait(3)
        for item in searhItems:
            query = {
                'query': item,
                'where': 'news',
                'ie': 'utf8',
                'sm': 'nws_hty'
            }
            params = parse.urlencode(query)
            url = naverSearchUrl + '?' + params

            browser.get(url)
            page = browser.page_source
            parser = BeautifulSoup(page, 'html.parser')            
            li_list = parser.select('ul.type01 > li')                

            newsCollection = []
            for li in li_list:
                a = li.select_one('dl > dt > a')        
                url = str(a.attrs['href'])
                if url in self.urls:
                    continue
                title = str(a.attrs['title'])
                dd = li.select('dl > dd')
                publisher = str(dd[0].select_one('span._sp_each_source').text)
                preview = str(dd[1].text)    
                
                news = {
                    'title' : title,
                    'url' : url,
                    'publisher' : publisher,
                    'preview' : preview        
                }
                self.urls.append(url)
                newsCollection.append(news)
        browser.close()
        return newsCollection