# Python 唯一支持的参数传递模式是共享传参（call by sharing）。多数面
# 向对象语言都采用这一模式，包括 Ruby、Smalltalk 和 Java（Java 的引
# 用类型是这样，基本类型按值传参）。

#call by sharing
def f(a, b):
    a += b
    return a

x = 1
y = 2
print(f(x, y))
print(x, y)
a = [1, 2]
b = [3, 4]
print(f(a, b))
print(a, b)
t = (10, 20)
u = (30, 40)
print(f(t, u))
print(t, u)