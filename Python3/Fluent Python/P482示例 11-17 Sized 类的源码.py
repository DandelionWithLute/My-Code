# 示例 11-17 Sized 类的源码，摘自 Lib/_collections_abc.py（Python
# 3.4，https://hg.python.org/cpython/file/3.4/Lib/_collections_abc.py#l127）
class Sized(metaclass=ABCMeta):
    __slots__ = ()

    @abstractmethod
    def __len__(self):
        return 0

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Sized:
            if any("__len__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented