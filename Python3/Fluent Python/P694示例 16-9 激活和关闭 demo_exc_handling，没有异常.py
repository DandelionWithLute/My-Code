class DemoException(Exception):
    """为这次演示定义的异常类型。"""

def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received:{!r}'.format(x))
    raise RuntimeError('This line should never run')

exc_coro = demo_exc_handling()
print(next(exc_coro))
print(exc_coro.send(11))
print(exc_coro.send(22))
exc_coro.close()
from inspect import getgeneratorlocals
print(getgeneratorlocals(exc_coro))
#Python3.4 'GEN_CLOSED'
#Python3.10     None
#               {}