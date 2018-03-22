# 한국생산기술연구원_사업공고
import requests
from bs4 import BeautifulSoup
import re

posts = list()
baseURL = 'https://www.kitech.re.kr/research/'
pageURL = 'https://www.kitech.re.kr/research/page1-1.php?page=1'
def Scraping():
    with requests.Session() as s:   
        req = s.get(pageURL)
        if req.ok:
            html = req.text
            bs = BeautifulSoup(html, 'html.parser')
            result = bs.find("table", {"class":"table_board"}).find('tbody')('tr')
            for item in result: #게시판의 number ~ date 까지 변수에 저장
                columns = item('td')
                postNumber = columns[0].get_text().strip()
                title = columns[1].find('a').get_text().strip()
                date = columns[3].get_text().strip()
                sourceURL = columns[1].find('a').get('href')
                contentURL = baseURL + sourceURL
                print(postNumber, title, date, contentURL)
                posts.append([6, int(postNumber), title, date, contentURL])
    return posts

