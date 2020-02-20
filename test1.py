from selenium import webdriver
from time import sleep
import random
import requests
from bs4 import BeautifulSoup
from operator import eq
import sys


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



a = input()
#접속되었을때 user ID얻는 함수
def userId():
    res = requests.get("https://kkutu.co.kr/?server=0")
    res.encoding = "utf-8"
    html = res.text
    userId= BeautifulSoup(html, "html.parser")
    #userId = str(userId)
    #k = userId.select('.div class')
    Id = html.find_all(id='UserMessage')
    #Id = userId.find("UserMessage")
    print(Id)

    #print(userId)



#sleep(30) 

##userId()
#kkutu_source = driver.page_source
#print(kkutu_source.index("UserMessage")) #print(kkutu_source.find("UserMessage"))
#print(kkutu_source[kkutu_source.index("UserMessage"):kkutu_source.index("UserMessage") + 16])
kkutu_source = driver.page_source
source = kkutu_source.index("UserMessage") #print(kkutu_source.find("UserMessage"))
source = kkutu_source[kkutu_source.index("UserMessage"):kkutu_source.index("UserMessage") + 16]
xpath = '//*[@id="' + source + '"]'
print(xpath)
print(type(xpath))

print("게임종료!!")


source = driver.page_source
print(source)
print("\n")
source = source[source.find("round-current"):]
source = source[source.find(">")+1:]
source = source[:source.find("<")]
print(source)
