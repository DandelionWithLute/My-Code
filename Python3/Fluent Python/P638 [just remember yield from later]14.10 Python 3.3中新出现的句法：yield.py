def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i

s = 'ABC'
t = tuple(range(3))
print(list(chain(s, t)))
############
a = [1,2,3,4,5]
b = ['A', 'B', 'C']
print(a, b)
#c = list(range(3))
c = tuple(range(3))
d = 'CDE'
print(c, d)