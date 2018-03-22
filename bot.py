import telegram
import scraper1
import scraper2
import scraper3
import scraper4
import scraper5
# import scraper6
# import scraper7
import scraper8
import scraper9
# import scraper10

webDic = dict() #각 사이트 별(rank1), 해당 사이트 게시글 별(rank2), 해당 게시글 정보들(rank3)을 담고있는 Dictionary

class WebSite():
    def __init__(self, webSiteNumber, Scraping): #Scraping은 각 사이트 Scraper 파일에 있는 function을 callback
        self.webSiteNumber = webSiteNumber
        self.Scraping = Scraping

    def SetDic(self):
        webDic[self.webSiteNumber] = dict() # 딕셔너리 안의 딕셔너리 형태        

class Post():
    def __init__(self, webSiteNumber, postNumber, title, date, contentURL):
        self.webSiteNumber = webSiteNumber
        self.postNumber = postNumber
        self.title = title
        self.date = date
        self.contentURL = contentURL

    def SaveData(self): # 딕셔너리에 Data 저장 
        webSiteIndex = self.webSiteNumber
        postIndex = self.postNumber
        webDic[webSiteIndex][postIndex] = dict() #삼 중 딕셔너리 형태
        webDic[webSiteIndex][postIndex][0] = self.postNumber 
        webDic[webSiteIndex][postIndex][1] = self.title
        webDic[webSiteIndex][postIndex][2] = self.date
        webDic[webSiteIndex][postIndex][3] = self.contentURL
        
    def Describe(self): # 딕셔너리에 있는 데이터 return
        webSiteIndex = self.webSiteNumber
        postIndex = self.postNumber
        postNumber = "postNumber : " + str(webDic[webSiteIndex][postIndex][0]) + "\n"
        title = "title : " + webDic[webSiteIndex][postIndex][1] + "\n"
        date = "date : " + webDic[webSiteIndex][postIndex][2] + "\n"
        contentURL = "contentURL : " + webDic[webSiteIndex][postIndex][3] + "\n"
        return(postNumber + title + date + contentURL + "\n\n")

def Write(webSiteInstance, fileName): #텍스트 파일에 Data 쓰기
    webSiteInstance.SetDic()
    posts = webSiteInstance.Scraping
    f = open(fileName, 'w', encoding='UTF-8')
    for i in posts:
        post = Post(i[0], i[1], i[2], i[3], i[4])       
        post.SaveData()
        f.write(post.Describe())
    f.close()

def Bot(fileName, ScraperFunc, webSiteNum): #봇 알림 기능
    try: 
        f = open(fileName, "r", encoding='UTF-8')
        line = f.readline()
        f.close()
        oldNum = int(line[13:].strip()) # 예전 Number
        Write(WebSite(webSiteNum, ScraperFunc), fileName)
        keyList = list(webDic[webSiteNum].keys())
        keyList.sort()
        newNum = int(keyList[-1]) # 현재 number
        if newNum > oldNum : # 새로운 게시글이 있으면 새로운 게시글 모두 알림
            for num in range(oldNum + 1, newNum + 1):
                title = webDic[webSiteNum][num][1]
                URL = webDic[webSiteNum][num][3]
                sendText = '*' + title + '*' + ' ' + '[link]' + '(' + URL + ')'
                bot.send_message(chat_id=user_chat_id, text=sendText, parse_mode=telegram.ParseMode.MARKDOWN)
               
    except: # 해당 사이트 스크레핑 처음일 때 txt에 Data 저장; 봇 알림 기능 없음
        Write(WebSite(webSiteNum, ScraperFunc), fileName)


if __name__ == '__main__':

    botToken = '522567929:AAGV7VsDYu9kBqaEjSdiSeK23fAGRUnmrYc' #werooringBot의 토큰
    bot = telegram.Bot(token = botToken)   #bot 선언
    user_chat_id = '530269193'
    Bot("scraper1.txt", scraper1.Scraping(), 1)
    Bot("scraper2.txt", scraper2.Scraping(), 2)
    Bot("scraper3.txt", scraper3.Scraping(), 3)
    Bot("scraper4.txt", scraper4.Scraping(), 4)
    Bot("scraper5.txt", scraper5.Scraping(), 5)
#   Bot("scraper6.txt", scraper6.Scraping(), 6)
#   Bot("scraper7.txt", scraper7.Scraping(), 7)
    Bot("scraper8.txt", scraper8.Scraping(), 8)
    Bot("scraper9.txt", scraper9.Scraping(), 9)
#   Bot("scraper10.txt", scraper10.Scraping(), 10)
