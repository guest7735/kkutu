import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.naver.com/")
html = BeautifulSoup(res.text, "html.parser")
print(html)
