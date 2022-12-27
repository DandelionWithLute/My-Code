from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img',
    {'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
for image in images:
    print(image['src'])

#../img/gifts/img1.jpg
#../img/gifts/img2.jpg
#../img/gifts/img3.jpg
#../img/gifts/img4.jpg
#../img/gifts/img6.jpg
