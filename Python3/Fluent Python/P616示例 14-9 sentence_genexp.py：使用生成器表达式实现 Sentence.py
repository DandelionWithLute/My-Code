import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))


# 与示例 14-7 唯一的区别是 __iter__ 方法，这里不是生成器函数了
# （没有 yield），而是使用生成器表达式构建生成器，然后将其返回。
# 不过，最终的效果一样：调用 __iter__ 方法会得到一个生成器对象。
# 生成器表达式是语法糖：完全可以替换成生成器函数，不过有时使用生
# 成器表达式更便利。下一节说明生成器表达式的用途。
