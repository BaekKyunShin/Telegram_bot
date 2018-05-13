import requests
from bs4 import BeautifulSoup
import re

dicWeb = dict()
class Post():
    def __init__(self, number, title, author, date, content, URL):
        self.number = number
        self.title = title
        self.author = author
        self.date = date
        self.content = content
        self.URL = URL

    def Describe(self):
        number = "number : " + self.number + "\n"
        title = "title : " + self.title + "\n"
        author = "author : " + self.author + "\n"
        date = "date : " + self.date + "\n"
        content = ""
        if type(self.content) == list: #content가 리스트형태이면 그림파일이고, 리스트가 아니라면 글형태임
            for url in self.content:
                content += "content : " + str(url) + "\n"
        else: content = "content : " + self.content + "\n"
        result = number + title + author + date + content + "\n\n" 
        return(result)
    
    def Save(self):
        index = int(self.number)
        content =''
        dicWeb[index] = dict() #딕셔너리 안의 딕셔너리 형태
        dicWeb[index][0] = self.number
        dicWeb[index][1] = self.title
        dicWeb[index][2] = self.author
        dicWeb[index][3] = self.date
        if type(self.content) == list: #content가 리스트형태이면 그림파일이고, 리스트가 아니라면 글형태임
            for url in self.content:
                content += str(url) + "\n"
        else: content = self.content + "\n"
        dicWeb[index][4] = content
        dicWeb[index][5] = self.URL



posts = list()
numberList = list()
baseURL = 'https://www.innopolis.or.kr/'
pageURL = 'sub0403/articles/index/tableid/m_bid/page/'

def Scraping():
    for pageOffset in range(1, 2):
        URL = baseURL + pageURL + str(pageOffset)
        req = requests.get(URL)
        if req.ok:
            html = req.text
            bs = BeautifulSoup(html, 'html.parser')
            result = bs.find("table", {"class":"base_table board_table"})('tbody')[0]('tr')
            for item in result: #게시판의 number ~ date 까지 변수에 저장
                columns = item('td')
                number = columns[0].get_text().strip()
                title = columns[2].get_text().strip()
                author = columns[3].get_text().strip()
                date = columns[4].get_text().strip()
                numberList.append(number)

                contentURL = columns[2].find("ul", {"class":"ellipsis_area"}).find("li",{"class":"ellipsis"}).find("a").get("href") #각 게시글의 컨텐츠 URL 저장
                URL = baseURL + contentURL
                req2 = requests.get(URL)
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
                            posts.append(Post(number, title, author, date, str(content), URL))

                        except: #예외적 태그 형태
                            result2 = bs2.find("td", {"class":"tx-content-container padding15"})
                            content = result2.get_text() 
                            posts.append(Post(number, title, author, date, str(content), URL))
                            

                    else: #게시글이 그림 형태일 때
                        posts.append(Post(number, title, author, date, urlList, URL)) 


def DoDescribe():
    Scraping()
    f = open("scraper1.txt", 'w', encoding='UTF-8')
    for post in posts:
        f.write(post.Describe())
        post.Save()
        
