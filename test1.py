from selenium import webdriver
from time import sleep
import random
import requests
from bs4 import BeautifulSoup
from operator import eq


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
#f = open("kkutu_co_kr.txt", encoding="utf-8")
#result = []
#for line in f:
#    result.append(line)

#접속되었을때 user ID얻는 함수
def userId():
    res = requests.get("https://kkutu.co.kr/?server=0")
    res.encoding = "utf-8"
    html = res.text
    userId= BeautifulSoup(html, "html.parser")
    userId = str(userId)
    #k = userId.select('.div class')
    Id = userId.find("UserMessage")
    print(Id)

    #print(userId)



#sleep(30) 

userId()

print("게임종료!!")