class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind

import weakref
stock = weakref.WeakKeyDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
                Cheese('Brie'), Cheese('Permesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese

print(sorted(stock.keys()))
del catalog
print(sorted(stock.keys()))
del cheese
print(sorted(stock.keys))