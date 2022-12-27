from urllib.request import urlopen
from urllib.error import HTTPError
try:
 html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
 print(e)
 # 返回空值，中断程序，或者执行另一个方案
else:
 # 程序继续。注意：如果你已经在上面异常捕捉那一段代码里返回或中断（break），
 # 那么就不需要使用else语句了，这段代码也不会执行