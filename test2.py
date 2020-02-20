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
    """
    source = source[source.find("round-current"):]
    print(source)
    source = source[source.find(">")+1:]
    print(source)
    source = source[:source.find("<")]
    print(source)
    """
    return source

for i in range(1, 100):
    a = input()
    if a == "finish":
        break
    print(getCurrentRounds())