from bs4 import BeautifulSoup
import requests
url = "https://yo-movies.com/"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html,"lxml")

s = str(soup.title)
s = s.replace("<title>","")
s = s.replace("</title>","")
print(s)