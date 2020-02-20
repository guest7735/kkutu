from selenium import webdriver
import time
import random
import requests
from bs4 import BeautifulSoup

message = ""
word = ""
#라운드마다 사용한 단어
list_ = []

driver = webdriver.Chrome("chromedriver.exe")
#driver.implicity_wait(3)
driver.get("https://kkutu.co.kr/?server=0")

#사전 텍스트 데이터 불러오기
f = open("kkutu_co_kr.txt", encoding="utf-8")
result = []
for line in f:
    result.append(line)

#현재 라운드가 어딘지 얻는 함수
def getCurrentRounds():
    kkutu_source = driver.page_source
    if kkutu_source.find("rounds-current") == -1:
        return False
    source = kkutu_source.index("rounds-current")
    source = kkutu_source[source + 16 : source + 17]
    return source


#현재 자신의 차례인지 아닌지 판단
def get_style(str):
    return driver.find_element_by_xpath(str).get_attribute("style")

#현재의 단어를 얻는 함수
def now():
    element = driver.find_elements_by_class_name('jjo-display')
    print(element[0])
    return element[0].text

    #공격하는 함수
def attack(start):
    
    word_list = get_word(start)
    """
    if len(word_list) == 0:
        print("찾을 수 없음")
        start = start.split('(')[0]
        word_list = get_word(start)
        return

    length = len(word_list)
    if length > 10:
        length = 5

    i = random.randrange(0, length)
    """
    message = word_list#[i]

    #print(message)
    send(message) #send함수 실행


    #특정 글자로 시작하는 단어를 찾아 긴 순서대로 출력합니다.
def get_word(start):
    text_list = []
    for i in result:
        if i.startswith(start):
            text = i
            if len(text) >= 2:
                text_list.append(text)

    text_list.sort(key=lambda item: (len(item), item), reverse=True) #정렬부분
    return text_list[0]

    #단어를 작성해서 보내는 함수
def send(message):
    print(message)
    input_tag = driver.find_element_by_xpath(userId())
    input_tag.send_keys(message + "\n")
    time.sleep(0.2)
    #click_tag = driver.find_element_by_xpath('//*[@id="ChatBtn"]')
    #click_tag.click()
    #각 라운드마다 사용한 단어 모으기
    list_.append(message)
    #각 라운드마다 사용한 단어 없애기
    result.remove(message)
    print(list_)
    

#접속되었을때 user ID얻는 함수
def userId():
    kkutu_source = driver.page_source
    source = kkutu_source.index("UserMessage") #print(kkutu_source.find("UserMessage"))
    source = kkutu_source[kkutu_source.index("UserMessage"):kkutu_source.index("UserMessage") + 16]
    xpath = '//*[@id="' + source + '"]'
    return xpath

def del_list_():
    global word
    global list_
    global result
    word_ = getCurrentRounds()
    if word_ != word:
        print(list_)
        result += list_
        list_ = []
        word = getCurrentRounds()
        print("\n")
        print(list_)


a = input()
#입력해야 게임 타이핑 시작!
word = getCurrentRounds()
print(word)

while True:
    try:
        if "none" in get_style('//*[@id="GameBox"]/div/div[3]'):
            del_list_()

            continue
        if "block" in get_style('//*[@id="GameBox"]/div/div[3]'):
            del_list_()
            
            #현재 시작 단어 구하기
            start = now()
            print(start)#눈으로 확인하기 위해 잠깐 출력함
            if '(' in start:
                start = start[2:3]
                """
                if len(word_list) == 0:
                    start = start.split('(')[0]
                    word_list = get_word(start)
                """
                #start = start.split('(') #륨(윰) 이렇게 되어있으면 맨 처음에는 '(' 시작 괄호로 나누면 ["륨", "윰)"] 이렇게 됌
                #start = start[1].split(')') #["륨", "윰)"] 이런 리스트에서 [1], 즉 두번째 원소를 ")" 끝 괄호로 split하면 "윰" 만 남는다
                #start = start[0]
            if len(start) == 1:
                attack(start)
        #안되는 경우 찾고 조금씩 정비하기
    except:
        time.sleep(1)


print("게임종료!!")
print(list_)
