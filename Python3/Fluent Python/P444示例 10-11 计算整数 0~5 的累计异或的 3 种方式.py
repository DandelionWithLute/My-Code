n = 0
for i in range(1, 6):
    n ^= i

print(n)


a = 2 ^ 5
print(a)

import functools
functools.reduce(lambda a, b : a^b, range(6))

import operator
functools.reduce(operator.xor, range(6))