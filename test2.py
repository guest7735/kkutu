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

def get():
    h_w_source = driver.page_source
    source = h_w_source.index("ellipse history-item expl-mother")
    source_end = h_w_source.index("history-class")
    source = source + 55
    source_end = source_end - 15
    h_w = h_w_source[source : source_end]
    list_ += h_w
    print(list_)
    
a = input()

get()