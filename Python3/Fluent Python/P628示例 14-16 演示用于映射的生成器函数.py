sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
print(list(enumerate('albatroz', 1)))
import operator
print(list(map(operator.mul, range(11), range (11))))
print(list(map(operator.mul, range(11), [2, 4, 8])))
print(list(map(lambda a,b: (a, b), range(11), [2, 4, 8])))
import itertools
print(list(itertools.starmap(lambda a, b: b/a,
    enumerate(itertools.accumulate(sample), 1))))