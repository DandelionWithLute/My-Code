print(all([1, 2, 3]))
print(all([1, 0, 3]))
print(all([]))
print(any([1, 2, 3]))
print(any([1, 0, 3]))
print(any([0, 0.0]))
#
print(any([0.1, 0.1]))
#
print(any([]))
g = (n for n in [0, 0.0, 7, 8])
print(any(g))
print(next(g))#why it jumped 7 directly
#!!!
a = [1,2,3,4,5]
print(next(a))
#!!!