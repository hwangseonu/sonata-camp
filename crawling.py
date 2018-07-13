from crawler import crawler
from crawler import merger


if __name__ == '__main__':
    crawler.crawl('https://comic.naver.com/webtoon/detail.nhn?titleId=318995&no=372&weekday=fri')
    merger.merge()
