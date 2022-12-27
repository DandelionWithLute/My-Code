import itertools
print(list(itertools.groupby('LLLLAAGGG')))
for char, group in itertools.groupby('LLLLAAAGG'):
    print(char, '->', list(group))
animals = ['rat', 'bat', 'duck', 'bear', 'lion', 'eagle', 'shark', 'giraffe', 'dolphin']
for length, group in itertools.groupby(reversed(animals), len):
    print(length, '->', list(group))