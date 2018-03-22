# 정보통신기술진흥센터
import requests
from bs4 import BeautifulSoup
import re

posts = list()
baseURL = 'https://www.iitp.kr' 
URL = 'https://www.iitp.kr/kr/1/notice/bid.it'

def Scraping():
    with requests.Session() as s:
        req = s.get(URL)
        if req.ok:
            html = req.text
            bs = BeautifulSoup(html, 'html.parser')
            result = bs.find("table", {"class":"table one-title"})('tbody')[0]('tr')
            for item in result: #게시판의 number ~ date 까지 변수에 저장
                columns = item('td')
                postNumber = columns[0].get_text().strip()
                title = columns[1].get_text().strip()
                date = columns[3].get_text().strip()
                sourceURL = columns[1].find("a").get("onclick")
                contentURL = baseURL + sourceURL.split("'")[1]
                contentURL = contentURL[:43] + contentURL[95:]
                posts.append([2, int(postNumber), title, date, contentURL])
    return posts