import itertools
print(list(itertools.chain('ABC', range(2))))
print(list(itertools.chain(enumerate('ABC'))))
print(list(itertools.chain.from_iterable(enumerate('ABC'))))
print(list(zip('ABC', range(5))))
print(list(itertools.zip_longest('ABC', range(5))))
print(list(itertools.zip_longest('ABC', range(5), fillvalue='?')))