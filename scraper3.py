# 한국과학기술정보연구원
import requests
from bs4 import BeautifulSoup
import re

posts = list()
baseURL = 'https://www.kisti.re.kr'
pageURL = '/notifications/post/research-task?t=1518746505506'

def Scraping():
    with requests.Session() as s:
        URL = baseURL + pageURL
        req = s.get(URL)
        if req.ok:
            html = req.text
            bs = BeautifulSoup(html, 'html.parser')
            result = bs.find_all("div", {"class":"bbs_list board-item"})
            for item in result: #게시판의 number ~ date 까지 변수에 저장
                columns = item('div')
                postNumber = columns[0].get_text().strip()
                title = columns[1].find('a').get_text().strip()
                date = columns[1].find("div", {"class":"text_info"}).find("span", {"class":"date"}).get_text().strip()
                sourceURL = columns[1].find('a').get('href')
                contentURL = baseURL + sourceURL
                posts.append([3, int(postNumber), title, date, contentURL])
    return posts

