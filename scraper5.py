# 한국과학창의재단_입찰공고
import requests
from bs4 import BeautifulSoup
import re

posts = list()
baseURL = 'https://www.kofac.re.kr'
pageURL = '/?page_id=1674'

def Scraping():
    with requests.Session() as s:
        URL = baseURL + pageURL
        req = s.get(URL)
        if req.ok:
            html = req.text
            bs = BeautifulSoup(html, 'html.parser')
            result = bs.find("div", {"class":"kboard-list"}).find("table", {"class":"list"}).find('tbody')('tr')
            for item in result: #게시판의 number ~ date 까지 변수에 저장
                columns = item('td')
                postNumber = columns[0].get_text().strip()
                title = columns[1].find('a').get_text().strip()
                date = columns[4].get_text().strip()
                sourceURL = columns[1].find('a').get('href')
                contentURL = baseURL + sourceURL
                posts.append([5, int(postNumber), title, date, contentURL])
    return posts

