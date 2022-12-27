# 方法解析顺序使用 C3 算法计算。Michele Simionato 的论文“The
# Python 2.3 Method Resolution
# Order”（https://www.python.org/download/releases/2.3/mro/）对
# Python 方法解析顺序使用的 C3 算法做了权威论述。如果对方法解
# 析顺序的细节感兴趣，可以阅读延伸阅读中给出的资料。不用过分
# 担心，C3 算法不难理解，Simionato 写道：
# ……除非大量使用多重继承，或者继承关系不同寻常，否则不
# 用了解 C3 算法，因此也不用阅读这篇论文。
# 结束对方法解析顺序的讨论之前，我们来看看图 12-2。这幅图展示了
# Python 标准库中 GUI 工具包 Tkinter 复杂的多重继承图。研究这幅图
# 时，要从底部的 Text 类开始。这个类全面实现了多行可编辑文本小组
# 件，它自身有丰富的功能，不过也从其他类继承了很多方法。左边是常
# 规的 UML类图。右边加入了一些箭头，表示方法解析顺序。使用示例
# 12-8 中定义的便利函数 print_mro 得到的输出如下：
print(bool.__mro__)
def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))
import tkinter
print_mro(tkinter.Text)
#Text, Widget, BaseWidget, Misc, Pack, Place, Grid, XView, YView, object