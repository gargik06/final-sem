#web crawling and indexing of web pages

import requests
from bs4 import BeautifulSoup

print("Performed by 740_Pallavi & 743_Deepak")
print("Crawling https://wikipedia.com")

html = requests.get("https://www.wikipedia.org/").text
soup = BeautifulSoup(html,"html.parser")

langs=["en","ja","de"]
for l in langs:
    print("Crawling https://"+l+".wikipedia.org/")
