@decorate
def target1():
    print('running target()')

def target2():
    print('running target()')

target2 = decorate(target2)