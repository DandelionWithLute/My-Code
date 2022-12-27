def vowel(c):
    return c.lower() in 'aeiou'

print(list(filter(vowel, 'Aardvark')))
import itertools
print(list(itertools.filterfalse(vowel, 'Aardvark')))
print(list(itertools.dropwhile(vowel, 'Aardvark')))
# Drop items from the iterable while predicate(item) is true.
# Afterwards, return every element until the iterable is exhausted.
print(list(itertools.takewhile(vowel, 'Aardvark')))
print(list(itertools.islice('Aardvark', 4)))
print(list(itertools.islice('Aardvark', 4, 7)))
print(list(itertools.islice('Aardvark', 1, 7, 2)))