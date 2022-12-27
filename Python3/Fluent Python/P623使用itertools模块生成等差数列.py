import itertools
gen = itertools.count(1, .5)
# for i in range(4):
#     print(next(gen))
gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
print(list(gen))