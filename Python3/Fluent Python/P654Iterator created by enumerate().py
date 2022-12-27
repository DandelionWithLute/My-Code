# 第一方面是接口。Python 的迭代器协议定义了两个方
# 法：__next__ 和 __iter__。生成器对象实现了这两个方法，因
# 此从这方面来看，所有生成器都是迭代器。由此可以得知，内置的
# enumerate() 函数创建的对象是迭代器：
from collections import abc
e = enumerate('ABC')
print(isinstance(e, abc.Iterator))

import types
e = enumerate('ABC')
print(isinstance(e, types.GeneratorType))