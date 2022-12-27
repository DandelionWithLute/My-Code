def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)

fact = factorial
print(fact)
print(fact(5))
print(map(factorial, range(11)))#range starts from 0
print(list(map(fact, range(11))))