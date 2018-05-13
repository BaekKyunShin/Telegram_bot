import telegram
import main

botToken = '522567929:AAGV7VsDYu9kBqaEjSdiSeK23fAGRUnmrYc' #werooringBot의 토큰
bot = telegram.Bot(token = botToken)   #bot을 선언합니다.
user_chat_id = '530269193'

try:
    f = open("scraper1.txt", "r", encoding='UTF-8')
    line = f.readline()
    f.close()
    oldNum = int(line[9:].strip()) # 예전 Number

    scraper.DoDescribe() # 현재 기준 스크레핑하기
    newNum = int(scraper.numberList[0]) # 현재 number
    
    if newNum > oldNum : # 새로운 게시글이 있으면 새로운 게시글 모두 프린트
        for num in range(oldNum + 1, newNum + 1):
            title = scraper.scraper1Dic[num][1]
            URL = scraper.scraper1Dic[num][5]
            sendText = '*' + title + '*' + ' ' + '[link]' + '(' + URL + ')'
            bot.send_message(chat_id=user_chat_id, text=sendText, parse_mode=telegram.ParseMode.MARKDOWN)

except:
    scraper.DoDescribe() # 현재 기준 스크레핑하기

'''testNum = int(scraper1.numberList[0])r
scraper1.DoScraping()

if testNum == scraper1.numberList[0] :
    print("OK")'''

'''
updates = bot.getUpdates()
lastUpdate = updates[-1]

print(lastUpdate.message.chat.id)
for update in updates:
    print(update)

for update in updates:
    print(update.message.text) #update는 json포맷 ; JSON은 속성-값 쌍으로 이루어진 데이터 오브젝트를 전달하기 위해 인간이 읽을 수 있는 텍스트를 사용하는 개방형 표준 포맷이다
'''