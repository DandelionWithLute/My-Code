import collections
class Text(collections.UserString):

    def __repr__(self) -> str:
        return 'Text({!r})'.format(self.data)

    def reverse(self):
        return self[::-1]
word = Text('forward')
print(word)
#❶ Text 实例的 repr 方法返回一个类似 Text 构造方法调用的字符串，
# 可用于创建相同的实例。
print(word.reverse())
#❷ reverse 方法返回反向拼写的单词。
# print(word.reverse(Text('backward'))) Outdated in new versions
print(type(Text.reverse), type(word.reverse))
print(list(map(Text.reverse, ['repaid', (10, 20, 30), Text('stressed')])))
print(6)
print(Text.reverse.__get__(word))
# ❻ 函数都是非覆盖型描述符。在函数上调用 __get__ 方法时传入实
# 例，得到的是绑定到那个实例上的方法。
print(7)
print(Text.reverse.__get__(None, Text))
# ❼ 调用函数的 __get__ 方法时，如果 instance 参数的值是 None，那
# 么得到的是函数本身。
print(8)
print(word.reverse)
# ❽ word.reverse 表达式其实会调用
# Text.reverse.__get__(word)，返回对应的绑定方法。
print(word.reverse.__self__)
#❾ 绑定方法对象有个 __self__ 属性，其值是调用这个方法的实例引用。
print(word.reverse.__func__ is Text.reverse)
#函数会变成绑定方法，这是 Python 语言底层使用描述符的最好例证。
