from bs4 import BeautifulSoup
import requests
#안녕하세요
res = requests.get("https://kkutu.co.kr/?serer=0")
res.encoding = "utf-8"
html = res.text
userId= BeautifulSoup(html, "html.parser")
k = userId.select('.div class')
print(k)


#hello!!
#my name is sukjun

