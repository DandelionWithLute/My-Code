def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)
fact = factorial
print(list(map(fact, range(6))))
print(list(factorial(n) for n in range(6)))
print(list(factorial(n) for n in range(6) if n % 2))