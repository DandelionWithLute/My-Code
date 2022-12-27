Lambda 函数非常实用，你甚至可以用它来替代现有的 BeautifulSoup 函数：
bs.find_all(lambda tag: tag.get_text() ==
 'Or maybe he\'s only resting?')
如果不使用 Lambda 函数，代码如下：
bs.find_all('', text='Or maybe he\'s only resting?')