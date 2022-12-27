print(zip(range(3), 'ABC'))
print(list(zip((range(3), 'ABC'))))
#[(range(0, 3),), ('ABC',)] The comma after )is different from python3.6
print(list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3])))
from itertools import zip_longest
print(list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], fillvalue=-1)))
