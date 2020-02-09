from selenium import webdriver
from time import sleep
import random
import requests
from bs4 import BeautifulSoup


driver = webdriver.Chrome("chromedriver.exe")
#driver.implicity_wait(3)
driver.get("https://kkutu.co.kr/?server=0")


#print("let's start!!")
#sleep(3)
#for i in range(10):
#    print(now())
#    sleep(10)

#//*[@id="ChatBtn"]
#//*[@id="Talk"]

#사전 텍스트 데이터 불러오기
f = open("kkutu_co_kr.txt", encoding="utf-8")
result = []
for line in f:
    result.append(line)

#현재의 단어를 얻는 함수
def now():
    element = driver.find_elements_by_class_name('jjo-display')
    return element[0].text

#접속되었을때 user ID얻는 함수
def userId():
    res = requests.get("https://kkutu.co.kr/?server=0")
    res.encoding = "utf-8"
    html = res.text
    userid = BeautifulSoup(html, "html.parser")


#특정 글자로 시작하는 단어를 찾아 긴 순서대로 출력합니다.
def get_word(start):
    text_list = []
    for i in result:
        if i.startswith(start):
            text = i
            if len(text) >= 2:
                text_list.append(text)

    text_list.sort(key=lambda item: (len(item), item), reverse=True) #정렬부분
    return text_list


#단어를 작성해서 보내는 함수
def send(message):
    print()
    print(message)
    #input_tag = driver.find_element_by_xpath('//*[@id="game-input"]')  //*[@id="UserMessage75325"]
    #input_tag.send_keys(message)
    #click_tag = driver.find_element_by_xpath('//*[@id="ChatBtn"]')
    #click_tag.click()

def get_style(str):
    return driver.find_element_by_xpath(str).get_attribute("style")
    #내차례인지 아닌지 판단하는 조건문 만들기

#공격하는 함수
def attack(start):
    word_list = get_word(start)
    if len(word_list) == 0:
        print("찾을 수 없음")
        return

    length = len(word_list)
    if length > 10:
        length = 5

    i = random.randrange(0, length)
    message = word_list[i]
    send(message) #send함수 실행

sleep(60)

while True:
    if "none" in get_style('//*[@id="GameBox"]/div/div[3]'):
        continue
    if "block" in get_style('//*[@id="GameBox"]/div/div[3]'):
        
        #현재 시작 단어 구하기
        start = now()
        print(start)#눈으로 확인하기 위해 잠깐 출력함
        if '(' in start:
            start = start.split('(')[0] #'(' 이 여는 괄호를 기준으로 앞에 있는 단어 하나만 가져온다.
        if len(start) == 1:
            attack(start)

print("게임종료!!")