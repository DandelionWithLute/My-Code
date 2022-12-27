# Alex 在他写的“水禽和抽象基类”一文中指出，即便不注册，抽象基类也
# 能把一个类识别为虚拟子类。下面是他举的例子，我添加了一些代码，
# 使用 issubclass 做测试：
class Struggle:
    def __len__(self): return 23

from collections import abc
print(isinstance(Struggle(), abc.Sized))
print(isinstance(Struggle, abc.Sized))
print(issubclass(Struggle, abc.Sized))