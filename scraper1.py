# 연구개발특구진흥재단
import requests
from bs4 import BeautifulSoup
import re

posts = list()
baseURL = 'https://www.innopolis.or.kr/'
pageURL = 'sub0403/articles/index/tableid/m_bid/page/'

def Scraping():
    for pageOffset in range(1, 2):
        URL = baseURL + pageURL + str(pageOffset)
        with requests.Session() as s:
            req = s.get(URL)
            if req.ok:
                html = req.text
                bs = BeautifulSoup(html, 'html.parser')
                result = bs.find("table", {"class":"base_table board_table"})('tbody')[0]('tr')
                for item in result: #게시판의 number ~ date 까지 변수에 저장
                    columns = item('td')
                    postNumber = columns[0].get_text().strip()
                    title = columns[2].get_text().strip()
                    date = columns[4].get_text().strip()
                    sourceURL = columns[2].find("ul", {"class":"ellipsis_area"}).find("li",{"class":"ellipsis"}).find("a").get("href") #각 게시글의 컨텐츠 URL 저장
                    
                    contentURL = baseURL + sourceURL
                    posts.append([1, int(postNumber), title, date, contentURL])
    return posts


'''                req2 = requests.get(contentURL)
                if req2.ok:
                    html2 = req2.text
                    bs2 = BeautifulSoup(html2, 'html.parser')               
                    images = bs2.find_all("img", {"src":re.compile(".*/attach.*/board/.*\.[jpg|png|bmp|gif]")}) #정규 표현식
                    urlList = list()
                    for image in images:
                        urlList.append(baseURL + image["src"])
                    if len(urlList) == 0 : #게시글이 글 형태일 때  
                        try: #기본 태그 형태
                            result2 = bs2.find("table", {"class":"txc-wrapper"}).find("td", {"bgcolor":"#ffffff"})
                            content = result2.get_text() 
                            posts.append(Post(number, title, date, str(content), URL))

                        except: #예외적 태그 형태
                            result2 = bs2.find("td", {"class":"tx-content-container padding15"})
                            content = result2.get_text() 
                            posts.append(Post(number, title, date, str(content), URL))
                            

                    else: #게시글이 그림 형태일 때
                        posts.append(Post(number, title, date, urlList, URL)) 
def DoDescribe():
    Scraping()
    f = open("scraper1.txt", 'w', encoding='UTF-8')
    for post in posts:
        f.write(post.Describe())
        post.Save()
'''
        
