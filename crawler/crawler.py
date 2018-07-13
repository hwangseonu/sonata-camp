import requests
import os
import shutil
from bs4 import BeautifulSoup as bs


def crawl(url):
    req = requests.get(url)
    soup = bs(req.text, 'html.parser')
    titles = soup.select(
        '#comic_view_area > div.wt_viewer > img'
    )
    directory = os.path.dirname('./img/')
    if not os.path.exists(directory):
        os.mkdir(directory)
    for i in range(len(titles)):
        img = soup.find('img', {'id': 'content_image_%d' % i})
        img_src = img.get('src')
        img_name = '%d.jpg' % i
        req = requests.get(img_src, stream=True, headers={'User-agent': 'Mozilla/5.0'})
        if req.status_code == 200:
            with open('./img/%s' % img_name, 'wb') as f:
                req.raw.decode_content = True
                shutil.copyfileobj(req.raw, f)
