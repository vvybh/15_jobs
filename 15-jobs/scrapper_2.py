import requests
from bs4 import BeautifulSoup

def search_incruit(keyword, pages):


keyword = "파이썬"
url = f"https://www.jobkorea.co.kr/Search?stext={keyword}&tabType=recruit&Page_No=1"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup)