import abc
class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """从可迭代对象中添加元素。"""

    @abc.abstractmethod
    def pick(self):
        """随机删除元素，然后将其返回。
        如果实例为空，这个方法应该抛出`LookupError`。
        """
        return bool(self.inspect())

    def loaded(self):
        """如果至少有一个元素，返回`True`，否则返回`False`。"""
        return bool(self.inspect())

    def inspect(self):
        """返回一个有序元组，由当前元素构成。"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))

from random import randrange

@Tombola.register
class TomboList(list):
    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')
        
    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))
print(Tombola.register(TomboList))

print(issubclass(TomboList, Tombola))
t = TomboList(range(100))
print(isinstance(t, Tombola))