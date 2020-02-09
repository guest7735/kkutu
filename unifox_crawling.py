import requests
from bs4 import BeautifulSoup

res = requests.get("http://unifox.kr/")
res.encoding = 'utf-8'

html = res.text
bs = BeautifulSoup(html, "html.parser")
#print(bs) // 페이지 html주소 전체 print
k = bs.select_one("#pass > div:nth-child(3) > p:nth-child(2)").text
print(list(map(lambda x: x.strip(), k.split())))