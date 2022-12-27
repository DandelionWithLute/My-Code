class DoppelDict(dict):
    # def __setitem__(self, __key: _KT, __value: _VT) -> None:
    #     return super().__setitem__(__key, __value)
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

dd = DoppelDict(one=1)
print(dd)
dd['two'] = 2
print(dd)
dd.update(three=3)
print(dd)

