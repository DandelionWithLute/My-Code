import itertools
def f():
    def do_yield(n):
        yield n
    x = 0
    while True:
        x += 1
        do_yield(x)
        #infinite loop -> do_yield(x)