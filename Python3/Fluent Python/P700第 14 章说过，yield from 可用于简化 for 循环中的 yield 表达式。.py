def gen():
    for c in 'AB':
        yield c
    for i in range(1, 3):
        yield i
print(list(gen()))

def gen():
    yield from 'AB'
    yield from range(1, 3)
#USE THIS INSTEAD OF THE FORMER ONE
print(list(gen()))