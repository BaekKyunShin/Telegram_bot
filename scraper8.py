# 한국항공우주연구원
import requests
from bs4 import BeautifulSoup
import re

posts = list()
baseURL = 'https://kpms.kari.re.kr'
pageURL = 'https://kpms.kari.re.kr/project/announcement.do'
def Scraping():
    with requests.Session() as s:
        req = s.get(pageURL)
        if req.ok:
            html = req.text
            bs = BeautifulSoup(html, 'html.parser')
            result = bs('tr')[1:]
            for item in result: #게시판의 number ~ date 까지 변수에 저장
                columns = item('td')
                postNumber = columns[0].get_text()[5:].strip()
                title = columns[1].find('a').get_text().strip()
                date = columns[6].get_text().strip()
                sourceURL = columns[1].find('a').get('href')
                contentURL = baseURL + sourceURL
                posts.append([8, int(postNumber), title, date, contentURL])
    return posts