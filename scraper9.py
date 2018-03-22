# 한국연구재단
import requests
from bs4 import BeautifulSoup
import re

posts = list()
baseURL = 'https://www.nrf.re.kr/tender/'
pageURL = 'https://www.nrf.re.kr/tender/list?menu_no=57'

def Scraping():
    with requests.Session() as s:   
        req = s.get(pageURL) # Session()으로 하는 것이 req = requests.get(pageURL) 보다 효율적
        if req.ok:
            html = req.text
            bs = BeautifulSoup(html, 'html.parser')
            result = bs.find('div', {"class":"board_list"}).find('tbody')('tr')
            for item in result: #게시판의 number ~ date 까지 변수에 저장
                columns = item('td')
                postNumber = columns[0].get_text().strip()
                title = columns[3].find('a').get_text().strip()
                date = columns[2].get_text().strip()
                sourceURL = columns[3].find('a').get('data-nts_no')
                contentURL = baseURL + 'view?nts_no='+sourceURL+'&menu_no=57&nts_no=&search_type=&search_keyword=&page='
                posts.append([9, int(postNumber), title, date, contentURL])
    return posts
