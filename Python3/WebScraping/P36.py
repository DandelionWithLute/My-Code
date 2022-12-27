from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html_parser')

nameList = bs.findAll('span', {'class':'green'})
for name in nameList:
 print(name.get_text())