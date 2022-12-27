#generator function
def gen_123():
    yield 1
    yield 2
    yield 3
print(gen_123)
print(gen_123())
for i in gen_123():
    print(i)

g = gen_123()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#❽ 生成器函数的定义体执行完毕后，生成器对象会抛出StopIteration 异常。
