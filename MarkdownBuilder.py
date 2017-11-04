import time
from os import path
from datetime import datetime
from NewsCrawler import NewsCrawler
from Modules import getDate

class MarkDownBuilder:
    def __init__(self, searchUrl, clips, interval = 3):
        self.searchUrl = searchUrl
        self.clips = clips
        self.interval = interval
    
    def build(self, filename=''):
        crawler = NewsCrawler()
        if len(filename) == 0:
            date = getDate()

        filename = path.dirname(__file__) + date + '_news.md'
        print(filename)
        with open(filename, 'w', encoding='utf-8') as f:
            for clip in self.clips:
                newsCollection = crawler.get(self.searchUrl, self.clips[clip])
                f.write("## {0}\n".format(clip))
                for news in newsCollection:
                    f.write("#### [{0}]({1}) - *{2}*\n".format(news["title"], news["url"], news["publisher"]))
                    f.write(news["preview"] + '\n\n')
                time.sleep(self.interval)
        return filename