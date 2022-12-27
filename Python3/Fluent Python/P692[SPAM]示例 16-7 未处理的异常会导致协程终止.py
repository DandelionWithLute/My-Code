def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count
coro_avg = averager()

#from coroaverager1 import averager

coro_avg = averager()
print(coro_avg.send(40))
print(coro_avg.send(50))
print(coro_avg.send('spam'))
print(coro_avg.send(60))