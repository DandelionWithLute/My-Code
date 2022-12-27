"""
用于计算移动平均值的协程
>>> coro_avg = averager() ➊
>>> from inspect import getgeneratorstate
>>> getgeneratorstate(coro_avg) ➋
'GEN_SUSPENDED'
>>> coro_avg.send(10) ➌
10.0
>>> coro_avg.send(30)
20.0
>>> coro_avg.send(5)
15.0
"""

from functools import wraps

def coroutine(func):
    """装饰器：向前执行到第一个`yield`表达式，预激`func`"""
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield averager
        total += term
        count += 1
        averager = total/count