import requests
from bs4 import BeautifulSoup

res = requests.get("https://kkutu.co.kr/?server=0")
html = BeautifulSoup(res.text, "html.parser")
#print(html)
print(html.find_all(class_="my-stat-name ellipse"))